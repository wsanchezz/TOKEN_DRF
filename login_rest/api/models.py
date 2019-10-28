from django.db import models

# Create your models here.
class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=15)
    apellido = models.CharField('Apellido', max_length=15)
    
    def __str__(self): #Como va a mostrar los datos
        return '{0},{1}'.format(self.apellido, self.nombre)