# Generated by Django 5.0.2 on 2024-02-25 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_alter_reserv_mest_parkovki_mesto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserv_mest_parkovki',
            name='mesto',
            field=models.CharField(max_length=50, verbose_name='Nazvanie'),
        ),
        migrations.AlterField(
            model_name='reserv_mest_parkovki',
            name='user',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='User'),
        ),
    ]
