from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('coopadd/', views.coopadd, name='coopadd')
]
