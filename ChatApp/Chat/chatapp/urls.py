from importlib.resources import path
from unicodedata import name
from django.urls import URLPattern
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:room>/', views.room, name='room'),
    path('checkview', views.checkview, name='checkview'),
]