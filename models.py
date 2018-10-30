from django.db import models

class Persona(models.Model):
    sexo = models.CharField(max_length=15)
    edad = models.IntegerField()
    sangre = models.CharField(max_length=2)

class Accidente(models.Model):
    fecha_hora = models.DateTimeField()
    latitud = models.DecimalField(max_digits=10,decimal_places=7)
    longitud = models.DecimalField(max_digits=10, decimal_places=7)
    personas = models.ManyToManyField(Persona)
