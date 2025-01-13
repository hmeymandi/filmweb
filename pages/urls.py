from django.urls import path
from .views import *

urlpatterns = [
    path('',testpages,name = 'page1')
]
