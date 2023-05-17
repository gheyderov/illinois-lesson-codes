from django.shortcuts import render, HttpResponse
from .models import Recipe, Category
from django.contrib import messages


# Create your views here.

def story(request):
    return render(request, 'stories.html')

def single(request):
    return render(request, 'single.html')

def recipe(request):
    print('Liked Posts: ', request.session.get('liked_posts'))
    recipes = Recipe.objects.all()
    categories = Category.objects.all()
    context = {
        'recipe_lists' : recipes,
        'categories' : categories

    }
    return render(request, 'recipes.html', context)

def create_story(request):
    return render(request, 'create_story.html')

# def like_post(request, pk):
#     messages.add_message(request, messages.SUCCESS, "Liked")
#     request.session['liked_posts'] = request.session.get('liked_posts', ' ') + str(pk) + ' '
#     return render(request, 'recipes.html')

def like_post(request, pk):
    response = HttpResponse('test')
    response.set_cookie('liked_posts', request.COOKIES.get('liked_posts', ' ') + str(pk) + ' ')
    return response