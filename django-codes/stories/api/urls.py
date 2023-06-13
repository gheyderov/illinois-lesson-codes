from django.urls import path
from stories.api.views import (
    categories, 
    recipes, 
    recipe_read_update,
    RecipeCreateAPIView,
    RecipeRetrieveUpdateDestroyAPIView
    )


urlpatterns = [
    path('categories/', categories, name='categories'),
    path('recipes/', RecipeCreateAPIView.as_view(), name='recipes'),
    path('recipes/<int:pk>/', RecipeRetrieveUpdateDestroyAPIView.as_view(), name='recipe_read_update'),

    
]