from __future__ import unicode_literals

from django.db import models

class Usuario(models.Model):
    id_usuario = models.IntegerField(max_length=2,unique=True)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    correo = models.EmailField()
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=7)
    rfc = models.CharField(max_length=11)

class Citas(models.Model):
    id_cita = models.IntegerField(max_length=2)
    id_usuario = models.ForeignKey(Usuario)
    fecha = models.DateField()
    tipo = models.CharField(max_length=10)
    confirmacion = models.BooleanField()

class Pedidos(models.Model):
    id_pedido = models.IntegerField(max_length=2)
    id_usuario = models.ForeignKey(Usuario)
    id_producto = models.ForeignKey(Productos)
    id_empleado = models.ForeignKey(Empleado)
    fecha_pedido = models.DateField()
    fecha_entrega = models.DateField()
    estatus = models.CharField(max_length=35)

class Ventas (models.Model):
    id_venta = models.IntegerField(max_length=2)
    id_usuario = models.ForeignKey(Usuario)
    id_empleado = models.ForeignKey(Empleado)
    id_producto = models.ForeignKey(Productos)
    cantidad = models.IntegerField()
    monto = models.FloatField(max_length=5)
    fecha = models.DateField()

class Factura(models.Model):
    id_factura = models.IntegerField(max_length=2)
    id_usuario = models.ForeignKey(Usuario)
    id_venta = models.ForeignKey(Ventas)

class Tipos de Cita(models.Model):
    id_cita = models.IntegerField(max_length=2)
    Inicial = models.BooleanField()
    Seguimiento = models.BooleanField()

class Productos(models.Model):
    id_producto = models.IntegerField(max_length=2)
    id_categoria = models.ForeignKey(Categoria)
    nombre = models.CharField(max_length=25)
    descripcion = models.TextField(max_length=150)
    cantidad = models.IntegerField(max_length=3)

class Categoria(models.Model):
    id_categoria = models.IntegerField(max_length=2)
    nombre = models.CharField(max_length=25)
    evento = models.CharField(max_length=20)