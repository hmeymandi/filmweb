from django.urls import path
from .views import *

urlpatterns = [
    path('',FilmListView.as_view(),name='filmlist'),
    path('detail/<slug:slug>', FilmDetailView.as_view(), name='filmdetail'),
]


