# Generated by Django 4.2.13 on 2024-05-25 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0004_rename_reserva_reserva_restaurante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva_restaurante',
            name='restaurante',
            field=models.CharField(max_length=100),
        ),
    ]
