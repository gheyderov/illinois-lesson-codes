from django.contrib import admin
from .models import (
    Recipe,
    Category,
    Tag,
    Comment
)

# Register your models here.

admin.site.register(Recipe)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)