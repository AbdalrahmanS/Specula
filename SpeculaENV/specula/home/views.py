from datetime import datetime

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from .forms import MoviePostForm
from .forms import TVPostForm
from .forms import VideoGamePostForm
from .models import MoviePost
from .models import TVPost
from .models import VideoGamePost


# Allows user to create post for TV section
class CreateTVPost(CreateView):
    model = TVPost
    success_url = 'tv'
    form_class = TVPostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# Allows user to create post for Movie section
class CreateMoviePost(CreateView):
    model = MoviePost
    success_url = 'movie'
    form_class = MoviePostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# Allows user to create post for Video Game section
class CreateVideoGamePost(CreateView):
    model = VideoGamePost
    success_url = 'videogame'
    form_class = VideoGamePostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# Shows all videogame posts
class VideoGameView(TemplateView):
    template_name = 'home/videogame.html'


# Shows all tv posts
class TView(TemplateView):
    template_name = 'home/tv.html'


# Shows all movie posts
class MovieView(TemplateView):
    template_name = 'home/movie.html'


# Shows the home view
class HomeView(TemplateView):
    template_name = 'home/welcome.html'



