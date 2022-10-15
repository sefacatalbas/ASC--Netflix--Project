from unicodedata import name
from django.urls import path     #Varan 9
from .views import *  #varan 10
# from . import views
"""
urlpatterns = [       
    path('', views.index, name='index'),
]
"""
urlpatterns = [       #varan 11
    path('', index, name='index'),
    path('movies/<str:slug>', movies, name='movies'),
    path('video/<int:id>', videolar, name= 'video'),
]