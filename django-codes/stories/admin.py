from django.contrib import admin
from .models import (
    Recipe,
    Category,
    Tag,
    Comment
)
from modeltranslation.admin import TranslationAdmin

# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)

@admin.register(Recipe)
class RecipeAdmin(TranslationAdmin):
    list_display = ['title', 'category', 'get_tags']

    def get_tags(self, obj):
        arr = []
        for tag in obj.tags.all():
            arr.append(tag.title)
        return arr