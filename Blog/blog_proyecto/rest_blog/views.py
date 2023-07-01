from core.models import Publicacion
from .serializers import PublicacionSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST'])
def lista_publicaciones(request):
    if request.method == 'GET':
        publicaciones = Publicacion.objects.all()
        serializer = PublicacionSerializer(publicaciones, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PublicacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
