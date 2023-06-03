from django.db import models
from core.models import AbstractModel
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

User = get_user_model()

# Create your models here.

class Recipe(AbstractModel):
    category = models.ForeignKey('Category', related_name='recipes', on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField('Tag')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')

    title = models.CharField('title', max_length=100)
    image = models.ImageField('image', upload_to='recipe/')
    cover_image = models.ImageField('cover_image', upload_to='recipe/')
    small_description = models.CharField('small_description', max_length=155)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self, **kwargs):
        return reverse_lazy('recipe_detail', kwargs = {'pk': self.id})
    
    # class Meta:
    #     ordering = '-created_at',


class Comment(AbstractModel):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=255)


class Category(AbstractModel):
    title = models.CharField('title', max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
    

class Tag(AbstractModel):
    title = models.CharField('title', max_length=100)

    def __str__(self):
        return self.title