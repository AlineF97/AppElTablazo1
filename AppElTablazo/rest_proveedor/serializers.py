from rest_framework import serializers
from core.models import proveedor

class proveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = proveedor
        fields = ['ID', 'nombre', 'telefono', 'direccion', 'email', 'contrasenia', 'pais','categoria']
