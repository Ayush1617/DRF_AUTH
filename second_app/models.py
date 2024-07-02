from django.db import models

# Create your models here.
class Movies(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    storyline = models.CharField(max_length=200)
    duration = models.DurationField()
    IMDB_rating = models.IntegerField()
    cast = models.CharField(max_length=100)
    starring = models.CharField(max_length=100)
    available_on = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
   
class User (models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)
