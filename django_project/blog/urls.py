from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),# leave it empty to make it for home page
    path('about/', views.about, name='blog-about'),
]

