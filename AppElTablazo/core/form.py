from django.forms import ModelForm
from .models import proveedor, Categoria

class proveedoresForm(ModelForm):

    
    class Meta:
        model = proveedor
        fields = ['ID', 'nombre', 'telefono', 'direccion', 'email', 'contrasenia', 'pais','categoria']