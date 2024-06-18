from rest_framework.test import APITestCase
from django.contrib.auth.models import User, Permission
from rest_framework.authtoken.models import Token
from .models import Restaurante, Reserva_restaurante
from rest_framework import status, mixins
from django.urls import reverse

class RestauranteTests(APITestCase):
    def setUp(self):
        # Crear un usuario con los permisos
        self.user = User.objects.create_user(username='test', password='prueba')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.restaurante_data = {'nombre': 'Restaurante Test', 'direccion': 'Calle F 123', 'tipo_cocina': 'Italiana'}
        self.restaurante = Restaurante.objects.create(**self.restaurante_data)
        self.restaurante_url = reverse('restaurante-list')

        # Asignar permisos al usuario de ejemplo administrador
        permisos = ['view_restaurante', 'add_restaurante', 'change_restaurante', 'delete_restaurante']
        for permiso in permisos:
            self.user.user_permissions.add(Permission.objects.get(codename=permiso))

    def test_create_restaurante(self):
        response = self.client.post(self.restaurante_url, self.restaurante_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    

    def test_delete_restaurante(self):
        restaurante = Restaurante.objects.create(**self.restaurante_data)
        response = self.client.delete(reverse('restaurante-prueba', args= [restaurante.id]), format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_list_restaurantes(self):
        response = self.client.get(self.restaurante_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_restaurante(self):
        response = self.client.get(reverse('restaurante-detail', args=[self.restaurante.id]), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_update_restaurante(self):
    #     update_data = {'nombre': 'Restaurante Actualizado'}
    #     response = self.client.put(reverse('restaurante-prueba', args=[self.restaurante.id]), update_data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)


class ReservaRestauranteTests(APITestCase):
    def setUp(self):
        # Crear un usuario con los permisos 
        self.user = User.objects.create_user(username='test', password='prueba')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.restaurante_data = {'nombre': 'Restaurante Test', 'direccion': 'Calle F', 'tipo_cocina': 'Italiana'}
        self.restaurante = Restaurante.objects.create(**self.restaurante_data)
        self.reserva_data = {
            'nombre_reserva': 'Reserva Test',
            'restaurante': self.restaurante,
            'fecha': '2024-06-01',
            'hora': '12:00:00',
            'numero_personas': 4
        }
        self.reserva_url = reverse('reserva-list')

        # Asignar permisos al usuario de tipo cliente
        permisos = ['view_reserva_restaurante', 'add_reserva_restaurante', 'change_reserva_restaurante', 'delete_reserva_restaurante']
        for permiso in permisos:
            self.user.user_permissions.add(Permission.objects.get(codename=permiso))


    def test_delete_reserva(self):
        reserva = Reserva_restaurante.objects.create(**self.reserva_data)
        response = self.client.delete(reverse('reservas-prueba', args=[reserva.id]), format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    
    def test_create_reserva(self):
        # Obtener el ID del restaurante
        restaurante_id = self.restaurante.id
        # Usar el id para identificar el dato
        self.reserva_data['restaurante'] = restaurante_id
        response = self.client.post(self.reserva_url, self.reserva_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_list_reservas(self):
        response = self.client.get(self.reserva_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_reserva(self):
        reserva = Reserva_restaurante.objects.create(**self.reserva_data)
        response = self.client.get(reverse('reserva-detail', args=[reserva.id]), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_update_reserva(self):
    #     reserva = Reserva_restaurante.objects.create(**self.reserva_data)
    #     update_data = {'nombre_reserva': 'Reserva Actualizada', 'restaurante': 'prueba', 'fecha': '2024-06-01','hora': '12:00:00','numero_personas': 8}
    #     response = self.client.put(reverse('reservas-prueba', args=[reserva.id]), update_data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
