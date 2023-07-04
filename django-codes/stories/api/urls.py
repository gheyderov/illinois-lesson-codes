from django.urls import path
from stories.api.views import (
    categories, 
    recipes, 
    recipe_read_update,
    RecipeCreateAPIView,
    RecipeRetrieveUpdateDestroyAPIView,
    TagAPIView,
    SubscriberCreateAPIView
    )


urlpatterns = [
    path('categories/', categories, name='categories'),
    path('subscribers/', SubscriberCreateAPIView.as_view(), name='subcribers'),
    path('tags/', TagAPIView.as_view(), name='tags'),
    path('recipes/', RecipeCreateAPIView.as_view(), name='recipe_lists'),
    path('recipes/<int:pk>/', RecipeRetrieveUpdateDestroyAPIView.as_view(), name='recipe_read_update'),

    
]