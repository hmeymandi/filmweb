from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

class Livetv(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    link = models.URLField()
    image = models.ImageField(upload_to='livetv_images')
    star_date = models.DateField()

class Actors(models.Model):
    gender_ch =(('Male', 'Male'), ('Female', 'Female'),)

    full_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200,unique=True)
    image = models.ImageField(upload_to='actors_images')
    gender = models.CharField(max_length=6, choices=gender_ch)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_of_birth = models.DateField()
    biography = models.TextField()
    date_of_death = models.DateField(null=True, blank=True)
    date_of_birth_place = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
    

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
    genre = models.ManyToManyField(Genre,related_name='films')
    description = models.TextField()
    actors = models.ManyToManyField(Actors,related_name='films')
    rating = models.FloatField()
    image = models.ImageField(upload_to='film_images')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    download_link_480 = models.URLField(blank=True)
    download_link_720 = models.URLField(blank=True)
    download_link_1080 = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Series(models.Model):
    title = models.CharField(max_length=200)
    slug=models.SlugField(max_length=200, unique=True)
    release_date = models.DateField()
    director = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    genre = models.ManyToManyField(Genre,related_name='series')
    description = models.TextField()
    actors = models.ManyToManyField(Actors,related_name='series')
    rating = models.FloatField()
    image = models.ImageField(upload_to='serirs_images')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    download_link_480 = models.URLField(blank=True)
    download_link_720 = models.URLField(blank=True)
    download_link_1080 = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    Film_Starts =[('1','خیلی بد'),
                  ('2','بد'),
                  ('3','عادی'),
                  ('4','خوب'),
                  ('5','عالی')]                 
                                       
                  
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
    