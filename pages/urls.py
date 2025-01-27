from django.urls import path
from .views import *



urlpatterns = [
    path('',testpages,name = 'page1'),
    path('profile/<int:pk>', UpdateProgile.as_view(), name = 'user_profile'),
   
]