from django.shortcuts import redirect, render,HttpResponse,get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import CommentForm


from .models import *

# Create your views here.



class FilmListView(generic.ListView):
    model = Film
    queryset =Film.objects.all().order_by('-id')[:10]
    template_name = "film/listview.html"

class FilmDetailView(generic.DetailView):
    model = Film
    template_name = "film/detailview.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        context['film','comments'] = get_object_or_404(Film.objects.all(), slug=slug)
        context['comments'] = CommentForm()
        return context

class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm  
    

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        film_id = int(self.kwargs.get('film_id'))
        film =get_object_or_404(Film, id=film_id)
        obj.film = film
        

       
        return super().form_valid(form)
    

 
