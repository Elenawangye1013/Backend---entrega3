from rest_framework import serializers
from .models import Restaurante, Reserva_restaurante

# Se definen 2 serializer, uno para cada modelo y le introducimos los datos que vamos a recibir
class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = ["nombre", "direccion", "tipo_cocina"]

class Reserva_restauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva_restaurante
        fields = ["nombre_reserva", "restaurante", "fecha", "hora", "numero_personas"]