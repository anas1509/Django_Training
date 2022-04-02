from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# the default user model django provide does not has a field for a profile picture
# so we need to extend the user model and and the picture field by creating a one to one model between users and profile 

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)# if we delete the user the profile will be deleted, but if we delete the profile the user will not be deleted
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile' 

    def save(self):
        
        super().save()
        img = Image.open(self.image.path)
         # to scale down the image size
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        




# now we have to makemigrations as we to reflect the changes to the DB, we need to install Pillow to from pip, which is a modle to work with images
#Do not forget to register the model in admin.py