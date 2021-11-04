from django.db import models

class Cine(models.Model):
    centro_comercial = models.CharField(max_length=256)
    direccion = models.CharField(max_length=256)
    def _str_(self) -> str:
        return self.centro_comercial

class Sala(models.Model):
    cine = models.ForeignKey(Cine, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=256)
    numero_sala = models.CharField(max_length=5)

class Fila(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    fila = models.CharField(max_length=256)

class Pelicula(models.Model):
    nombre = models.CharField(max_length=256)
    duracion = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)

    
# Create your models here.
 


 
  
   
