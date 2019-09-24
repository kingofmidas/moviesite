from .models import Movie

def slider_movies(request):
    movies = Movie.objects.exclude(banner__isnull=True)
    print(movies)
    return {'slider_movie': movies}