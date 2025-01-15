from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Film(models.Model):
    title = models.CharField(max_length=200)
    slug=models.SlugField(max_length=200, unique=True)
    release_date = models.DateField()
    director = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE,related_name='films')
    description = models.TextField()
    rating = models.FloatField()
    image = models.ImageField(upload_to='film_images')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title