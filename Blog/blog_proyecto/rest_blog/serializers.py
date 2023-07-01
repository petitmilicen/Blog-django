from rest_framework import serializers
from core.models import Publicacion

class PublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = ['autor','titulo','categoria','texto']