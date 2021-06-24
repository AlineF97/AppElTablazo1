from .form import proveedoresForm
from .models import proveedor
from django.shortcuts import redirect, render

# Create your views here.

def list_proveedor(request):
    proveedores = proveedor.objects.all()
    datos = {
        "proveedores" : proveedores
    }
    return render(request, 'core/list_proveedor.html', datos)

def form_proveedor(request):
    datos = {
        'form' : proveedoresForm()
    }

    if request.method == 'POST':
        formulario = proveedoresForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardados correctamente"

    return render(request, 'core/form_proveedor.html', datos)


def mod_proveedor(request, id):

    proveedores = proveedor.objects.get(ID=id)

    datos = {
        'form' : proveedoresForm(instance=proveedores)
    }

    if request.method == 'POST':
        formulario = proveedoresForm(request.POST, instance=proveedores)
        if formulario.is_valid:
            formulario.save()
            datos['form'] = formulario
            datos['mensaje'] = "Modificados correctamente"

    return render(request, 'core/mod_proveedor.html', datos)

def form_del_proveedor(request, id):

    proveedores = proveedor.objects.get(ID=id)

    proveedores.delete()
    
    return redirect(to="Proveedores")


def index(request):
    return render(request, 'core/index.html')

def Mediterranea(request):
    return render(request, 'core/mediterranea.html')

def Griega(request):
    return render(request, 'core/Griega.html')

def Tropical(request):
    return render(request, 'core/tropical.html')

def QuienesSomos(request):
    return render(request, 'core/QuienesSomos.html')

def Formulario(request):
    return render(request, 'core/FormContacto.html')


