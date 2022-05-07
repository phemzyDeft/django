from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee_form'),
    path('list/', views.employee_list, name='employee_list'),
    path('', views.employee_delete, name='employee_delete'),
]