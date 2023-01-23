import datetime
import pytz

from django.shortcuts import render, get_object_or_404
# from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PostSerializer, CategorySerializer
from recipe.models import Post, Category

# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/recipe-list',
    }
    return Response(api_urls)


@api_view(['GET'])
def recipeList(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def categoriesTitle(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def categoryRecipeList(request, pk):
    category = Category.objects.get(id=pk)
    detail_category = category.recipe_categories.all()
    serializer = PostSerializer(detail_category, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def recipeRecommendationList(request):
    now = datetime.datetime.now(pytz.utc)
    current_hour = now.strftime("%H")

    if current_hour >= '12' and current_hour < '18':
        meals = Post.published.filter(meal__title='Lunch')
    elif current_hour >= '18' and current_hour < '6':
        meals = Post.published.filter(meal__title='Dinner')
    else:
        meals = Post.published.filter(meal__title='Breakfast')
    serializer = PostSerializer(meals, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def recipeRecommendationTitle(request):
    now = datetime.datetime.now(pytz.utc)
    current_hour = now.strftime("%H")

    if current_hour >= '12' and current_hour < '18':
        meal_title = "Lunch"
    elif current_hour >= '18' and current_hour < '6':
        meal_title = "Dinner"
    else:
        meal_title = "Breakfast"
    title = {
        meal_title,
    }
    return Response(title)


@api_view(['GET'])
def recipeDetail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published',
                             publish__year=year, publish__month=month, publish__day=day)
    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def recipeCreate(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
