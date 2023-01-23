from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Category(models.Model):
    title = models.CharField(max_length=250)
    icon = models.FileField(upload_to="icons/")
    alternativeIcon = models.ImageField(
        upload_to="alternativeIcons/", null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Meal(models.Model):
    title = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural = 'Meals'

    def __str__(self):
        return self.title


class Post(models.Model):
    objects = models.Manager()
    published = PublishedManager()

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='recipe_categories')
    slug = models.SlugField(
        max_length=250, unique_for_date='publish', editable=False)
    meal = models.ForeignKey(Meal, on_delete=models.PROTECT,
                             related_name='recipe_meals', null=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='recipe_posts')
    image = models.ImageField(null=True, blank=True,
                              upload_to='photos/%y/%m/%d/')
    ingredients = models.TextField()
    instructions = models.TextField()
    nutritions = models.TextField()
    minutes = models.IntegerField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def get_absolute_url(self):
        return reverse('recipe:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
