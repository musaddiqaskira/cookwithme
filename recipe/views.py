import datetime
import pytz

from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required

from .models import Post, Category, Meal


from django.contrib.postgres.search import SearchVector
from .forms import SearchForm

@login_required
def post_search(request):
    #test
    categories = Category.objects.all()
    posts = Post.published.all()
    #endtest
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.published.annotate(search=SearchVector('title', 'description'),
            ).filter(search=query)
    return render(request, 'recipe/post/search.html', {'form':form, 'query':query, 'results': results, 'categories': categories, 'posts': posts})


# Create your views here.

def post_list(request):
    categories = Category.objects.all()
    posts = Post.published.all()
    
    now = datetime.datetime.now(pytz.utc)
    current_hour = now.strftime("%H")

    if current_hour >= '12' and current_hour < '18':
        meals = Post.published.filter(meal__title = 'Lunch')
        meal_title = "Lunch"
    elif current_hour >= '18' and current_hour <'6': 
        meals = Post.published.filter(meal__title = 'Dinner')
        meal_title = "Dinner"
    else:
        meals = Post.published.filter(meal__title = 'Breakfast')
        meal_title = "Breakfast"
        
    return render(request, 'recipe/post/list.html', {'categories': categories, 'posts': posts, 'meals': meals,
    'meal_title': meal_title})

@login_required
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'recipe/post/detail.html', {'post':post})


def category_detail(request, pk):
    category = Category.objects.get(id=pk)
    detail_category = category.recipe_categories.all()

    return render(request, 'recipe/post/category.html', {'category':category, 'detail_category':detail_category})

@login_required
def profile(request):
    return render(request, 'recipe/post/profile.html', {} )

# @login_required
def shop(request):
    return render(request, 'recipe/post/shop/products.html', {})


class CreateView(CreateView):
    model = Post
    context_object_name = 'recipe'
    template_name='recipe/post/create.html'
    fields = ['title', 'description', 'category', 'meal', 'image', 'ingredients', 'instructions', 'nutritions', 'minutes', 'status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
