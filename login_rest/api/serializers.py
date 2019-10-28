#Convertir datos a un archivo Json
from rest_framework import serializers
from .models import Persona

class PersonaSerializer(serializers.ModelSerializer): #Que cree un serializador en base de un model(Persona)
    class Meta:
        model = Persona #El que vamos a usar
        fields = ('id', 'nombre', 'apellido')


        
     