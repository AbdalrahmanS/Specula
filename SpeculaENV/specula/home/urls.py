from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('movies', views.MovieView.as_view(), name='viewMovie'),
    path('movie', views.MovieView.as_view(), name='viewMovie'),
    path('tv', views.TView.as_view(), name='viewTV'),
    path('videogame', views.VideoGameView.as_view(), name='viewVideoGame'),
    path('moviePost', views.CreateMoviePost.as_view(), name='newMoviePost'),
    path('videoGamePost', views.CreateVideoGamePost.as_view(), name='newVideoGamePost'),
    path('tvPost', views.CreateTVPost.as_view(), name='newTVPost')
]
