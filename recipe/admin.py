from django.contrib import admin

from .models import Post, Category, Meal
# Register your models here.
admin.site.register(Category)
admin.site.register(Meal)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display  = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
