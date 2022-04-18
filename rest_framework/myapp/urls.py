from django.urls import path
from . import views


urlpatterns =[
    path("books/", views.BookList.as_view(), name='BookList'),
    path("books/<str:pk>", views.BookDetails.as_view(), name='BookList'),
]