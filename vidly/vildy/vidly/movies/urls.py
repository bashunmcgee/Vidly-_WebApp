from django.urls import path
from . import views
from .views import MovieListCreateAPIView
urlpatterns = [
    path('', views.index, name='movies_index'),
    path('<int:movie_id>', views.detail, name='movies_detail'),
    path('movies/', MovieListCreateAPIView.as_view(), name='movie-list-create')
]
