# Generated by Django 5.0.2 on 2024-03-05 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0004_alter_reserv_mest_parkovki_mesto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserv_mest_parkovki',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]