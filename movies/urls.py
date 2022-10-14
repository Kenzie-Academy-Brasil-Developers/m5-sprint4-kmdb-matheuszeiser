from django.urls import path

from .views import ListAndDeleteMovieView, MovieView

urlpatterns = [
    path("movies/", MovieView.as_view()),
    path("movies/<int:movie_id>/", ListAndDeleteMovieView.as_view()),
]
