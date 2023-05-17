from django.urls import path
from stories.views import story, single, recipe, create_story, like_post

urlpatterns = [
    path('stories/', story, name='stories'),
    path('single/', single, name='single'),
    path('recipes/', recipe, name='recipes'),
    path('like_post/<int:pk>/', like_post, name='like_post'),
    path('create_story/', create_story, name='create_story'),


]
