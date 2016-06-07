from __future__ import unicode_literals

from django.db import models

class Citas(models.Model):
#    tipo = (
#        ('Inicial', '1'),
#        ('Seguimiento', '2'),
#    )
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
#    tipo = models.CharField(choices=tipo, max_length=1)
    fecha = models.DateField()


class RegistroUsuario(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)


class Catalogo(models.Model):
    descripcion = models.TextField(max_length=50)
    apellido = models.ImageField(null=True, blank=True)
