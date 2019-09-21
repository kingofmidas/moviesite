from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie
# Create your views here.

class MovieList(ListView):
    model = Movie
   


class MovieDetail(DetailView):
    model = Movie