from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:country_name>', views.country, name='country'),
    path('tariff/', views.tariff, name='tariff'),
]
