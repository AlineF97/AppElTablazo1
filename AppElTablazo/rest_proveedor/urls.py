from django.urls import path
from rest_proveedor.views import lista_proveedores, detalle_proveedor

urlpatterns = [
    path('lista_proveedores', lista_proveedores, name="lista_proveedores"),
    path('detalle_proveedor/<id>', detalle_proveedor, name="detalle_proveedor"),
]
