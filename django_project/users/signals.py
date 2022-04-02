## This signal is to create a profile whenever a new user is created

from django.db.models.signals import post_save #this is a signal that fire after an object is saved
from django.contrib.auth.models import User # the user will be the sender of the signal
from django.dispatch import receiver # the reciver will recieve the signal and perform some task
from .models import Profile # we'll create a profile afetr user is created


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()