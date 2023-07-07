from typing import Any, Dict, Sequence
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from .models import Recipe, Category
from django.contrib import messages
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CommentForm, RecipeForm
from django.urls import reverse_lazy
from stories.tasks import export_data

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
        'recipe_list' : recipes,
        'categories' : categories

    }
    return render(request, 'recipes.html', context)


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes.html'
    context_object_name = 'recipes'
    paginate_by = 2


    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        cat_id = self.request.GET.get('category')
        tag_id = self.request.GET.get('tag')
        if cat_id:
            queryset = queryset.filter(category__id = cat_id)
        if tag_id:
            queryset = queryset.filter(tags__id = tag_id)
        return queryset

        


class RecipeDetailView(FormMixin, DetailView):
    model = Recipe
    template_name = 'single.html'
    form_class = CommentForm
    

    def get_success_url(self) -> str:
        return reverse_lazy('recipe_detail', kwargs = {'pk' : self.object.pk})

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        
    def form_valid(self, form: Any) -> HttpResponse:
        form.instance.recipe = self.object
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)
        



def create_story(request):
    return render(request, 'create_story.html')


class CreateRecipe(LoginRequiredMixin, CreateView):
    template_name = 'create_recipe.html'
    form_class = RecipeForm
    # success_url = reverse_lazy('home')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class UpdateRecipe(LoginRequiredMixin, UpdateView):
    template_name = 'create_recipe.html'
    form_class = RecipeForm
    model = Recipe
    # success_url = reverse_lazy('home')



# def like_post(request, pk):
#     messages.add_message(request, messages.SUCCESS, "Liked")
#     request.session['liked_posts'] = request.session.get('liked_posts', ' ') + str(pk) + ' '
#     return render(request, 'recipes.html')

def like_post(request, pk):
    response = HttpResponse('test')
    response.set_cookie('liked_posts', request.COOKIES.get('liked_posts', ' ') + str(pk) + ' ')
    return response


def export_view(request):
    export_data.delay()
    return HttpResponse('success')