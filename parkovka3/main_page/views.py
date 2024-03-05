from django.shortcuts import render
from reservation.models import Reserv_mest_parkovki
from django.db.models import Count

# Create your views here.

def main_with_map(request):
    return render(request, "main_page/map.html")

def free_space(request):
    free_space_count = Reserv_mest_parkovki.objects.filter(status = True).count()

    context = {
        'free_space_count': free_space_count,
    }


    return render(request, 'main_page/map.html', context)