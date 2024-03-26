from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_with_map, name='main_with_map'), # главная страница
    path('', views.free_space, name = 'mesta'),  # отображение свободных мест????
    path('reservation/', include('reservation.urls')),  # страница брони мест
]
