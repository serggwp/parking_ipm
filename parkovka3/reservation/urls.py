from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.reserv, name = 'reserv'),
    path('<int:pk>', views.registr_form.as_view(), name = 'registr'),
    path('return', views.return_def, name = 'return')
]
