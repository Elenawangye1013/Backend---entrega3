from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
# Definir las rutas a las que se pueden acceder
urlpatterns = [
    path('admin/', admin.site.urls),
    # en este caso indicamos el resto de urls a las que se pueden acceder

    path('api/', include("reservas.urls")),
    # path('auth/', obtain_auth_token)
]
