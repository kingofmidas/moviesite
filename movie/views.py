from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import YearArchiveView
from .models import Movie, MovieLinks
# Create your views here.


class HomeView(ListView):
    model = Movie
    template_name = 'movie/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['top_rated'] = Movie.objects.filter(status='tr')
        context['most_watched'] = Movie.objects.filter(status='mw')
        context['recently_added'] = Movie.objects.filter(status='ra')
        return context


class MovieList(ListView):
    model = Movie
    paginate_by = 2


class MovieDetail(DetailView):
    model = Movie

    def get_object(self):
        object = super().get_object()
        object.views_count += 1
        object.save()
        return object
    
    def get_context_data(self, **kwargs):
        context = super(MovieDetail, self).get_context_data(**kwargs)
        context['links'] = MovieLinks.objects.filter(movie=self.object)
        context['related_movies'] = Movie.objects.filter(category=self.object.category)


class MovieCategory(ListView):
    model = Movie
    paginate_by = 1

    def get_queryset(self):
        self.category = self.kwargs['category']
        movies = Movie.objects.filter(category=self.category)
        return movies

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie_category'] = self.category
        return context



class MovieLanguage(ListView):
    model = Movie
    paginate_by = 1

    def get_queryset(self):
        self.language = self.kwargs['lang']
        movies = Movie.objects.filter(language=self.language)
        return movies

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movie_language'] = self.language
        return context



class MovieSearch(ListView):
    model = Movie
    paginate_by = 1

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list = Movie.objects.filter(title__icontains=query)
        else:
            object_list = Movie.objects.none()
        return object_list

    
class MovieYear(YearArchiveView):
    queryset = Movie.objects.all()
    date_field = 'year_of_production'
    make_object_list = True
    allow_future = True