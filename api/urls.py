from django.urls import path
from . import views

app_name = "api"

urlpatterns = [
    path('', views.apiOverview, name="apiOverview"),
    path('recipe-list', views.recipeList, name="recipe-list"),
    path('category-title', views.categoriesTitle, name="category-title"),
    path('category-recipe-list/<int:pk>',
         views.categoryRecipeList, name="category-recipe-list"),
    path('recipe-recommendation-list',
         views.recipeRecommendationList, name="recipe-recommendation-list"),
    path('recipe-recommendation-title',
         views.recipeRecommendationTitle, name="recipe-recommendation-title"),
    path('recipe-detail/<int:year>/<int:month>/<int:day>/<slug:post>',
         views.recipeDetail, name="recipe-detail"),
    path('recipe-create', views.recipeCreate, name="recipe-create"),
]
