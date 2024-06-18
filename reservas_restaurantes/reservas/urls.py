from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    Reserva_restauranteCreateView,
    RestauranteCreateView,
    RestauranteListView,
    RestauranteRetrieveUpdateDestroy,
    RestauranteDetailView,
    RestauranteDeleteAllView,
    Reserva_restauranteListView,
    Reserva_restauranteRetrieveUpdateDestroy,
    Reserva_restauranteDetailView,
    Reserva_restauranteDeleteAllView,
    CreateReservaForRestauranteView,
    CustomAPIView,
    RestauranteViewSet,
)
# Se crea un router y registra el viewset
router = DefaultRouter()
router.register(r'restaurantes', RestauranteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #  get de la lista de restaurantes
    path('restaurantes/', RestauranteListView.as_view(), name='restaurante-list'), 
    # post de un restaurante
    path('restaurantes/create/', RestauranteCreateView.as_view(), name='restaurante-create'),
    # get un restaurante por el id
    path('restaurantes/<int:pk>/detail/', RestauranteDetailView.as_view(), name='restaurante-detail'),
    # put get, delete, put 
    path('restaurantes/<int:pk>/prueba/', RestauranteRetrieveUpdateDestroy.as_view(), name='restaurante-prueba'),
    # delete all
    path('restaurantes/deleteall/', RestauranteDeleteAllView.as_view(), name='restaurante-deleteall'),
    # post de reserva
    path('reservas/create/', Reserva_restauranteCreateView.as_view(), name='reserva-create'),
    #  get revervas
    path('reservas/', Reserva_restauranteListView.as_view(), name='reserva-list'),
    # get put delete
    path('reservas/<int:pk>/',Reserva_restauranteRetrieveUpdateDestroy.as_view(), name='reservas-prueba'),
    # get detail reserva
    path('reservas/<int:pk>/detail/', Reserva_restauranteDetailView.as_view(), name='reserva-detail'), 
    # deleteall reserva
    path('reservas/deleteall/', Reserva_restauranteDeleteAllView.as_view(), name='reserva-deleteall'), 
    # post para crear reservas y se relacionan con un resturante
    path('restaurantes/<int:restaurante_id>/reservas/', CreateReservaForRestauranteView.as_view(), name='relacion'),
    # get custom api y devuelve toda la info
    path('custom-api/', CustomAPIView.as_view(), name='custom-api')
]
