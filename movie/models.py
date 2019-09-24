from django.db import models
from django.utils import timezone

# Create your models here.
CATEGORY_CHOICES = (
    ('action', 'ACTION'),
    ('drama', 'DRAMA'),
    ('comedy', 'COMEDY'),
    ('romance', 'ROMANCE'),
)
LANGUAGE_CHOICES = (
    ('en', 'ENGLISH'),
    ('gr', 'GERMAN'),
)
STATUC_CHOICES = (
    ('ra', 'RECENTLY ADDED'),
    ('mw', 'MOST WATCHED'),
    ('tr', 'TOP RATED'),
)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='movies')
    banner = models.ImageField(upload_to='banner', blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=15)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2)
    status = models.CharField(choices=STATUC_CHOICES, max_length=2)
    year_of_production = models.DateField()
    views_count = models.IntegerField(default=0)
    cast = models.CharField(max_length=100)
    movie_trailer = models.URLField()
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

LINK_CHOICES = (
    ('D', 'DOWNLOAD LINK'),
    ('W', 'WATCH LINK'),
)
class MovieLinks(models.Model):
    movie = models.ForeignKey(Movie, related_name='movie_watch_link', on_delete=models.CASCADE)
    link = models.URLField(max_length=300)
    type = models.CharField(choices=LINK_CHOICES, max_length=1)

    def __str__(self):
        return self.movie
    class Meta:
        verbose_name_plural = 'Movie links'