from django.urls import path
from .views import home, contacto, galeria, agregar_solicitud, listar_solicitud, modificar_producto, eliminar_producto, registro, tecnico, listar_tecnico

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),
    path('agregar-solicitud/', agregar_solicitud, name="agregar_solicitud"),
    path('agregar-tecnico/', tecnico, name="agregar_tecnico"),
    path('listar-solicitud/', listar_solicitud, name="listar_solicitud"),
    path('listar-tecnicos/', listar_tecnico, name="listar_tecnicos"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('registro/', registro, name="registro"),
]
