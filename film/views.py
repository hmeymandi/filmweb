from django.shortcuts import render,HttpResponse,get_object_or_404
from django.views import generic


from .models import *

# Create your views here.



class FilmListView(generic.ListView):
    model = Film
    queryset =Film.objects.all()
    template_name = "film/listview.html"

class FilmDetailView(generic.DetailView):
    model = Film
    template_name = "film/detailview.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs.get('slug')
        context['film'] = get_object_or_404(Film.objects.all(), slug=slug)
        return context


