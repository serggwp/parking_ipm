from .models import Reserv_mest_parkovki
from django.forms import ModelForm, TextInput

# Форма брони места


class Reserv_Form(ModelForm):
    class Meta:
        model = Reserv_mest_parkovki
        fields = ['user', 'mesto', 'status']

        widgets = {
            'user': TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Login'}
            )
        }
