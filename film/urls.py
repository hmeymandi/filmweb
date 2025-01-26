from django.urls import path
from .views import *

urlpatterns = [
    path('',CombinedListView.as_view(),name='filmlist'),


    path('series/detail/<slug:slug>',SeriesDetailView.as_view(),name='seriesdetail'),
    path('film/detail/<slug:slug>', FilmDetailView.as_view(), name='filmdetail'),
    path('comment/film/<int:film_id>/',CommentCreateView.as_view(), name='comment_create' ),
    path('comment/series/<int:series_id>/',SeriesCommentCreateView.as_view(), name='comment_create1' ),
    path('filmlist/', CombinedListView.as_view(), {'template': 'template2'}, name='allfilmlist')
   
]


