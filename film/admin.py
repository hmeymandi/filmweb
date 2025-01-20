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
    list_display = ('title', 'release_date', 'director', 'genre', 'rating')
    list_filter = ('release_date', 'director', 'genre')
    search_fields = ('title', 'director', 'genre')
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