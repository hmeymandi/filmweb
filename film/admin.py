from django.contrib import admin
from .models import *

# Register your models here.

class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Genre, GenreAdmin)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'director', 'rating')
    list_filter = ('release_date', 'director', )
    search_fields = ('title', 'director',)
    date_hierarchy = 'release_date'
    ordering = ('title',)
    readonly_fields = ('date_created', 'date_modified')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Film,MovieAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('film', 'author', 'body', 'created_at')
    list_filter = ('film', 'author', 'created_at')
    search_fields = ('film', 'author', 'body')
         

admin.site.register(Comment, CommentAdmin)

class ActorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'date_of_birth', 'gender')
    list_filter = ('date_of_birth', 'gender')
    search_fields = ('full_name', 'date_of_birth')
    ordering = ('full_name',)
    prepopulated_fields = {'slug': ('full_name',)}


admin.site.register(Actors, ActorAdmin)

class LivetvAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'start_date',)
    list_filter = ('name', 'start_date',)
    search_fields = ('title', 'name')
    date_hierarchy = 'start_date'
    ordering = ('title',)
    prepopulated_fields = {'slug': ('title',)}

class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'director', 'rating')
    list_filter = ('release_date', 'director',)
    search_fields = ('title', 'director',)
    date_hierarchy = 'release_date'
    ordering = ('title',)
    readonly_fields = ('date_created', 'date_modified')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Series, SeriesAdmin)
