from unicodedata import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.payment, name='payment'),
    path('createorder/', views.createorder, name='createorder'),

]
