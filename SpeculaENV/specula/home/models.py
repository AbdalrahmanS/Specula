from django.db import models

# Create your models here.
class MoviePost(models.Model):
    posterName = models.CharField(max_length=200)
    movieName = models.CharField(max_length=200)
    opinion = models.TextField()

class TVPost(models.Model):
    posterName = models.CharField(max_length=200)
    tvShowName = models.CharField(max_length=200)
    opinion = models.TextField()

class VideoGamePost(models.Model):
    posterName = models.CharField(max_length=200)
    videoGameName = models.CharField(max_length=200)
    opinion = models.TextField()
