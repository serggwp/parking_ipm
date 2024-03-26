from django.shortcuts import render
from .models import Reserv_mest_parkovki
from django.views.generic import UpdateView

# страница брони мест
def reserv(request):
    mesta_status = Reserv_mest_parkovki.objects.all()
    return render(
        request, "reservation/reserv.html", {'mesta_status': mesta_status}
    )


# страница переадресации
def return_def(request):
    return render(request, 'reservation/return_html.html')


# бронь конкретного места, когда нажимаешь на него
class registr_form(UpdateView):
    model = Reserv_mest_parkovki
    template_name = 'reservation/login.html'
    fields = ['user', 'status']
    context_object_name = 'nomer_mesta'
