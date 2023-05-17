from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    bio = models.CharField('bio', max_length=150)
    image = models.ImageField('image', upload_to='media/user_profile')