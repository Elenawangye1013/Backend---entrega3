# Generated by Django 4.2.13 on 2024-05-25 10:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0003_reserva'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reserva',
            new_name='Reserva_restaurante',
        ),
    ]
