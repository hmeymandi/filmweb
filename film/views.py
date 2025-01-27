from django.shortcuts import redirect, render,HttpResponse,get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import CommentForm, SeriesCommentForm
from django.views.generic import TemplateView
from .models import Series, Film
from django.core.paginator import Paginator
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.



class CombinedListView(TemplateView):
    template_name = 'film/listview.html'
    def get_template_names(self):
        if self.kwargs.get('template') == 'template2':
            return ['film/filmlist.html']
        return [self.template_name]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['series1'] = Series.objects.all().order_by('-id')[:10]
        movie_list = Film.objects.all().order_by('-id')
        movie_paginator = Paginator(movie_list, 10) 
        page_number = self.request.GET.get('page')
        
        movie_page = movie_paginator.get_page(page_number)
        context['movies'] = movie_page
        return context


# class FilmListView(generic.ListView):
#     model = Film
#     queryset =Film.objects.all().order_by('-id')[:10]
#     context_object_name = "movies"
#     template_name = "film/listview.html"

# class SeriesListView(generic.ListView):
#     model = Series
#     queryset = Series.objects.all().order_by('-id')[:10]
#     context_object_name = "series1"
#     template_name = "film/listview.html"

from django.shortcuts import get_object_or_404
from django.views import generic

class SeriesDetailView(generic.DetailView):
    model = Series
    template_name = "film/seriesdetailview.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        series = self.object
        seasons = series.seasons.prefetch_related('episodes')
        context['series'] = series
        context['seasons'] = seasons
        slug = self.kwargs.get('slug')
        context['series','sereiscomments'] = get_object_or_404(Series.objects.all(), slug=slug)
        context['sereiscomments'] = CommentForm()  # فرم ارسال نظر جدید

        return context

    
class FilmDetailView(generic.DetailView):
    model = Film
    template_name = "film/detailview.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        context['film','comments'] = get_object_or_404(Film.objects.all(), slug=slug)
        context['comments'] = CommentForm()
        return context

class CommentCreateView(generic.CreateView, LoginRequiredMixin):
    model = Comment
    form_class = CommentForm  
    

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        film_id = int(self.kwargs.get('film_id'))                                   
        film =get_object_or_404(Film, id=film_id)
        obj.film = film     
       
        return super().form_valid(form)
    

class SeriesCommentCreateView(generic.CreateView,LoginRequiredMixin):
    model = SeriesComment
    form_class = SeriesCommentForm  
    

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        series_id = int(self.kwargs.get('series_id'))                                   
        series =get_object_or_404(Series, id=series_id)
        obj.series = series          
        return super().form_valid(form)
    
def genre(request):
    genres = Genre.objects.all()
    print(genres)
    context = {'genres': genres}
    return render(request, 'templates/_base.html', context=context)
