from django.urls import path
from stories.views import story, single, recipe, create_story, like_post, RecipeListView, RecipeDetailView, CreateRecipe, UpdateRecipe

urlpatterns = [
    path('stories/', story, name='stories'),
    path('single/', single, name='single'),
    path('recipes/', RecipeListView.as_view(), name='recipes'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('like_post/<int:pk>/', like_post, name='like_post'),
    path('create_story/', create_story, name='create_story'),
    path('create_recipe/', CreateRecipe.as_view(), name='create_recipe'),
    path('update_recipe/<int:pk>/', UpdateRecipe.as_view(), name='update_recipe'),


]
