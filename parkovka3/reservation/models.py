from django.db import models

# Create your models here.

class Reserv_mest_parkovki(models.Model):
        mesto =  models.CharField('Nazvanie', max_length = 50)
        status = models.BooleanField(default = True)
        user = models.CharField('User', max_length = 50, default = '', blank=True)

        def __str__(self):
            return self.mesto
        
        def get_absolute_url(self):
            return f'return'
    