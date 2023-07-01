from rest_framework import serializers
from core.models import Publicacion, Comentario

class PublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = ['autor','titulo','categoria','texto']
        
class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['autor','publicacion','texto']