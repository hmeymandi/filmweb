from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

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
    
class Comment(models.Model):
    Film_Starts =[('1','very_bad'),
                  ('2','bad'),
                  ('3','normal'),
                  ('4','good'),
                  ('5','very_good')]
                  
                  
                  
                  
                  
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='comments')           
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name='comments')
    body = models.TextField()
    stars = models.CharField(max_length=20, choices=Film_Starts)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.film.title}'
    
    def get_absolute_url(self):
        return reverse("filmdetail", args=[self.film.slug])
    