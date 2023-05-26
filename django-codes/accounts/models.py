from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    bio = models.CharField('bio', max_length=150, null=True, blank=True)
    image = models.ImageField('image', upload_to='media/user_profile', null=True, blank=True)

    def get_avatar(self):
        if self.image:
            return self.image.url
        else:
            return '/static/images/nophoto.jpeg/'