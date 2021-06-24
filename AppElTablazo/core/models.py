from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id de categoria")
    nombreCategoria = models.CharField(max_length=50, verbose_name="Nombre de la categoria")

    def __str__(self):
        return self.nombreCategoria

#Modelo para proveedor

class proveedor(models.Model):
    ID = models.CharField(max_length=6, primary_key=True, verbose_name="1.	Número de identificación")
    nombre = models.CharField(max_length=50, verbose_name="2.	Nombre completo")
    telefono = models.CharField(max_length=12, verbose_name="3.	Teléfono")
    direccion = models.CharField(max_length=50, verbose_name="4.	Dirección")
    email = models.CharField(max_length=50, verbose_name="5.	Email")
    contrasenia = models.CharField(max_length=12, null=False, blank=False, verbose_name="6.	Contraseña")
    pais = models.CharField(max_length=50, null=True, blank=True, verbose_name="7.	Pais")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.ID


   