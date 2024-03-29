from django.urls import path, include
from .views import *

app_name='movie'
urlpatterns = [
    path('', MovieList.as_view(), name='movie_list'),
    path('category/<str:category>', MovieCategory.as_view(), name='movie_category'),
    path('language/<str:lang>', MovieLanguage.as_view(), name='movie_language'),
    path('search/', MovieSearch.as_view(), name='movie_search'),
    path('year/<int:year>', MovieYear.as_view(), name='movie_year'),
    path('<slug:slug>', MovieDetail.as_view(), name='movie_detail')
]
