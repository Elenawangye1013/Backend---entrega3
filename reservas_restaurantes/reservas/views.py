
# from django.views.generic import CreateView, ListView

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Restaurante, Reserva_restaurante
from .serializers import RestauranteSerializer, Reserva_restauranteSerializer
from rest_framework import generics, permissions, authentication, status, viewsets

# crear y mostrar lista get y post de restaurantes con vista genérica
class RestauranteListView(generics.ListCreateAPIView):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]


# Detalle, Actualización y Eliminación de restaurantes con vista generica
class RestauranteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

class RestauranteViewSet(viewsets.ModelViewSet):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

# detail Muestra los detalles de un restaurante con vista generica
class RestauranteDetailView(generics.RetrieveAPIView):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]


# post de resuataurantes con api view
class RestauranteCreateView(APIView):
    def post(self, request):
        serializer = RestauranteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

# delete all, borrar todos los datos 
class RestauranteDeleteAllView(generics.GenericAPIView):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer

    def delete(self, request, *args, **kwargs):
        count, _ = self.get_queryset().delete()
        return Response({'message': f'{count} restaurantes fueron eliminados con éxito!'}, status=status.HTTP_204_NO_CONTENT)
#  POST RESERVA
class Reserva_restauranteCreateView(APIView):
    def post(self, request):
        serializer = Reserva_restauranteSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# GET RESERVAS

class Reserva_restauranteListView(generics.ListCreateAPIView):
    queryset = Reserva_restaurante.objects.all()
    serializer_class = Reserva_restauranteSerializer

# Detalle, Actualización y Eliminación

class Reserva_restauranteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva_restaurante.objects.all()
    serializer_class = Reserva_restauranteSerializer
    
    
# detail
class Reserva_restauranteDetailView(generics.RetrieveAPIView):
    queryset = Reserva_restaurante.objects.all()
    serializer_class = Reserva_restauranteSerializer

# delete all
class Reserva_restauranteDeleteAllView(generics.GenericAPIView):
    queryset = Reserva_restaurante.objects.all()
    serializer_class = Reserva_restauranteSerializer

    def delete(self, request, *args, **kwargs):
        count, _ = self.get_queryset().delete()
        return Response({'message': f'{count} reservas fueron eliminadas con éxito!'}, status=status.HTTP_204_NO_CONTENT)
# class RestauranteListView(APIView):
#     def get(self, request):
#         reservas = Restaurante.objects.all()
#         serializer =RestauranteSerializer(reservas, many = True)
#         return Response(serializer.data)
    
# class RestauranteRetrieveUpdateDestroy(APIView):
#     def get_object(self, pk):
#         try: 
#             return Restaurante.objects.get(pk=pk)
#         except Restaurante.DoesNotExist:
#             return None
        
#     def get(self, request, pk):
#         reserva = self.get_object(pk)
#         print(reserva)
#         if reserva is None:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = RestauranteSerializer(reserva)
#         return Response(serializer.data)
    
#     def delete(self, request, pk):
#         reserva = self.get_object(pk)
#         if reserva is None:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         reserva.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
#     def put(self, request, pk):
#         reserva = self.get_object(pk)
#         if reserva is None:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = RestauranteSerializer(reserva, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data ,status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#  Post dpara crear reservas
class CreateReservaForRestauranteView(APIView):
    def post(self, request, restaurante_id):
        try:
            restaurante = Restaurante.objects.get(id=restaurante_id)
        except Restaurante.DoesNotExist:
            return Response({'error': 'Restaurante no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        data = request.data.copy()
        data['restaurante'] = restaurante_id

        serializer = Reserva_restauranteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Get para ver todos los datos disponibles

class CustomAPIView(APIView):
    def get(self, request, format=None):
        restaurantes = Restaurante.objects.all()
        reservas = Reserva_restaurante.objects.all()
        restaurantes_serializer = RestauranteSerializer(restaurantes, many=True)
        reservas_serializer = Reserva_restauranteSerializer(reservas, many = True)
        return Response({
            'restaurantes': restaurantes_serializer.data,
            'reservas': reservas_serializer.data
        })
