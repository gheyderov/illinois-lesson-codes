from stories.models import Category, Recipe, Tag
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from stories.api.serializers import (
    CategorySerializer, 
    RecipeSerializer, 
    RecipeCreateSerializer,
    TagSerializer
    )
from rest_framework.decorators import api_view
from rest_framework.generics import (
    CreateAPIView, 
    ListAPIView, 
    ListCreateAPIView, 
    RetrieveUpdateDestroyAPIView
    )

def categories(request):
    category_list = Category.objects.all()
    # category_dict_list = []
    # for cat in category_list:
    #     category_dict_list.append({
    #         'cat_id' : cat.id,
    #         'title' : cat.title
    #     })
    serializer = CategorySerializer(category_list, many = True)
    return JsonResponse(data=serializer.data, safe=False)


class TagAPIView(ListAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class RecipeCreateAPIView(ListCreateAPIView):
    '''
        sample
    '''
    serializer_class = RecipeCreateSerializer
    queryset = Recipe.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RecipeSerializer
        return self.serializer_class
    

class RecipeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = RecipeCreateSerializer
    queryset = Recipe.objects.all()


@api_view(http_method_names = ['GET', 'POST'])
def recipes(request):
    if request.method == 'POST':
        serializer = RecipeCreateSerializer(data = request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data = serializer.data, safe=False, status = 201)
        return JsonResponse(data = serializer.errors, safe=False, status = 400)
    recipe_list = Recipe.objects.all()
    serializer = RecipeSerializer(recipe_list,  context={'request': request}, many = True)
    return JsonResponse(data = serializer.data ,safe=False)


@api_view(http_method_names = ['PUT', 'PATCH'])
def recipe_read_update(request, pk):
    if request.method == 'PUT':
        recipe = Recipe.objects.get(pk = pk)
        serializer = RecipeCreateSerializer(data = request.data, context={'request': request}, instance = recipe)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data = serializer.data, safe=False, status = 201)
        return JsonResponse(data = serializer.errors, safe=False, status = 400)
    if request.method == 'PATCH':
        recipe = Recipe.objects.get(pk = pk)
        serializer = RecipeCreateSerializer(data = request.data, partial = True, context={'request': request}, instance = recipe)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data = serializer.data, safe=False, status = 201)
        return JsonResponse(data = serializer.errors, safe=False, status = 400)
    