from django.contrib import admin
from core.models import Contact, BlockedIps, Subscribers

# Register your models here.

admin.site.register(Contact)
admin.site.register(BlockedIps)
admin.site.register(Subscribers)