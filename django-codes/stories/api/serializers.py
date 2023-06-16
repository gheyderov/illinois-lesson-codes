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
    category = CategorySerializer()
    tags = TagSerializer(many = True)
    class Meta:
        model = Recipe
        fields = (
            'id',
            'title',
            'category',
            'tags',
            'author_name',
            'slug',
            'image',
            'cover_image',
            'small_description',
            'description'
        )


class RecipeCreateSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    slug = serializers.SlugField(read_only=True)
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

    def validate(self, attrs):
        request = self.context['request']
        attrs['author'] = request.user
        return super().validate(attrs)