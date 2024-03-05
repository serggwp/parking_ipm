from django.shortcuts import render, redirect
from .models import Reserv_mest_parkovki
from .forms import Reserv_Form
from django.views.generic import UpdateView
from django.urls import reverse

def reserv(request):
    mesta_status = Reserv_mest_parkovki.objects.all()
    return render(request, "reservation/reserv.html", {'mesta_status': mesta_status})

def return_def(request):
    return render(request, 'reservation/return_html.html')

class registr_form(UpdateView):
    model = Reserv_mest_parkovki
    template_name = 'reservation/login.html'
    fields = ['user', 'status']
    context_object_name = 'article'

