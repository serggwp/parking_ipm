# Generated by Django 5.0.2 on 2024-02-25 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reserv_mest_parkovki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mesto', models.CharField(max_length=50, verbose_name='Nazvanie')),
                ('status', models.BooleanField(default=True)),
            ],
        ),
    ]
