from django import forms
from django.core.exceptions import ValidationError

from .models import MoviePost
from .models import TVPost
from .models import VideoGamePost


class MoviePostForm(forms.ModelForm):
    class Meta:
        model = MoviePost
        fields = ('posterName', 'movieName', 'opinion')
        widgets = {
            'posterName': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'movieName': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'opinion': forms.TextInput(attrs={'class': 'form-control my-5'})
        }
        labels = {
            'posterName': 'Your Alias',
            'movieName': 'Name of Movie',
            'opinion': 'Write your opinion here'
        }


class TVPostForm(forms.ModelForm):
    class Meta:
        model = TVPost
        fields = ('posterName', 'tvShowName', 'opinion')
        widgets = {
            'posterName': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'tvShowName': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'opinion': forms.TextInput(attrs={'class': 'form-control my-5'})
        }
        labels = {
            'posterName': 'Your Alias',
            'tvShowName': 'Name of TV Show',
            'opinion': 'Write your opinion here'
        }


class VideoGamePostForm(forms.ModelForm):
    class Meta:
        model = VideoGamePost
        fields = ('posterName', 'videoGameName', 'opinion')
        widgets = {
            'posterName': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'videoGameName': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'opinion': forms.TextInput(attrs={'class': 'form-control my-20'})
        }
        labels = {
            'posterName': 'Your Alias',
            'videoGameName': 'Name of Video Game',
            'opinion': 'Write your opinion here'
        }
