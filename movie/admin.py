from django.contrib import admin
from .models import Movie, MovieLinks
# Register your models here.

admin.site.register(MovieLinks)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year_of_production', 'status', 'language', 'category')
    list_filter = ('year_of_production', 'status', 'language', 'category')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}