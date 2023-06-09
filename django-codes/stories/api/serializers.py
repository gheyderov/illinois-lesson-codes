from rest_framework import serializers
from stories.models import Category, Recipe, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title'
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title'
        )


class RecipeSerializer(serializers.ModelSerializer):
    # category = serializers.CharField(source = 'category.title')
    # category = CategorySerializer()
    tags = TagSerializer(many = True)
    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'category',
            'tags',
            'author',
            'slug',
            'image',
            'cover_image',
            'small_description',
            'description'
        )