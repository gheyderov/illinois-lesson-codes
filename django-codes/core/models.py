from django.db import models
from .validators import validate_gmail

# Create your models here.

class AbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Contact(AbstractModel):
    name = models.CharField('Adiniz', max_length=100)
    email = models.EmailField('E-poct', max_length=30)
    subject = models.CharField('Movzu', max_length=100, null=True, blank=True)
    message = models.TextField()
    

    class Meta:
        ordering = '-created_at',

    def __str__(self) -> str:
        return self.name


class BlockedIps(models.Model):
    ip_address = models.GenericIPAddressField()