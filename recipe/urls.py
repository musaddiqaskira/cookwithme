from django.urls import path
from . import views

app_name = 'recipe'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>', views.post_detail, name='post_detail'),
    path('category/<int:pk>', views.category_detail, name="category_detail"),
    path('search/', views.post_search, name='post_search'),
    path('profile/', views.profile, name="profile"),
    path('shop/', views.shop, name="shop"),
    path('create/', views.CreateView.as_view(), name="new_recipe")
]