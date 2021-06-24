from django.contrib import admin

from core.models import Categoria, proveedor
from django.contrib import admin
from .models import Categoria, proveedor

# Register your models here.
admin.site.register(Categoria)
admin.site.register(proveedor)