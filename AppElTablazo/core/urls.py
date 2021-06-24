from django.urls import path
from .views import index, Formulario, Griega, Mediterranea, Tropical, QuienesSomos, list_proveedor,form_proveedor,mod_proveedor,form_del_proveedor

urlpatterns = [
    path('', index, name="index"),
    path('Formulario', Formulario, name="Formulario"),
    path('Griega', Griega, name="Griega"),
    path('Mediterranea', Mediterranea, name="Mediterranea"),
    path('Tropical', Tropical, name="Tropical"),
    path('QuienesSomos', QuienesSomos, name="QuienesSomos"),
    path('proveedores', list_proveedor, name="Proveedores"),
    path('form_proveedor', form_proveedor, name="form_proveedor"),
    path('mod_proveedor/<id>', mod_proveedor, name="mod_proveedor"),
    path('form_del_proveedor/<id>', form_del_proveedor, name="form_del_proveedor")

   
]