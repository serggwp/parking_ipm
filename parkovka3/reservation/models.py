from django.db import models

# Модель для парковочных мест, где статус -- занятое или свободное место, название -- номер ячейки


class Reserv_mest_parkovki(models.Model):
    mesto = models.CharField('Nazvanie', max_length=50)
    status = models.BooleanField(default=False)
    user = models.CharField('User', max_length=50, default='')

    def __str__(self):
        return self.mesto

    def get_absolute_url(self):
        return f'return'
