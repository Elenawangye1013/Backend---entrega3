from django.db import models

# Se definen dos modelos, uno de reataurantes y otro para las reservas de los restaurantes
# Se definen los campos de datos que se quieren incluir y el tipo de dato 
class Restaurante(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    tipo_cocina = models.CharField(max_length=100, default='Español')

    def __str__(self):
        return self.nombre

class Reserva_restaurante(models.Model):
    nombre_reserva = models.CharField(max_length=100)
    # restaurante = models.CharField(max_length=100)
    restaurante = models.ForeignKey(Restaurante, related_name='reservas', on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    numero_personas = models.PositiveIntegerField()
    def __str__(self):
        return self.nombre_reserva
