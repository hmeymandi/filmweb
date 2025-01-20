from django.urls import path
from .views import *

urlpatterns = [
    path('',FilmListView.as_view(),name='filmlist'),
    path('detail/<slug:slug>', FilmDetailView.as_view(), name='filmdetail'),
    path('comment/<int:film_id>/',CommentCreateView.as_view(), name='comment_create'  ),

   
]


