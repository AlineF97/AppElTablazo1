
# Create your views here.

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import proveedor
from .serializers import proveedorSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def lista_proveedores(request):
    """
    Lista todos los vehiculos
    """
    if request.method == 'GET':
        Proveedores = proveedor.objects.all()
        serializer = proveedorSerializer(Proveedores, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = proveedorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def detalle_proveedor(request, id):
    """
    get, update, delete de un vehiculo en particular
    """
    try:
        Proveedores = proveedor.objects.get(ID = id)
    except proveedor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = proveedorSerializer(Proveedores)
        return Response(serializer.data)        
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = proveedorSerializer(Proveedores, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data) 
    elif request.method == 'DELETE':
        Proveedores.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


