from django.db import models

class Usuario(models.Model):
    correo = models.CharField(max_length=50, null=False, blank=False)
    nombre= models.CharField (max_length=30, null=False, blank=False)
    usuario= models.CharField(max_length=30, null=False, blank=False)
    password= models.CharField(max_length=20, null=False, blank=False)
    telefono= models.IntegerField( null=False, blank=False)


class Encargado(models.Model):
    usuario = models.CharField(max_length=20, null=False, blank=False)
    password = models.CharField(max_length=20, null=False, blank=False)

class Cliente(models.Model):
    usuario = models.CharField(max_length=20, null=False, blank=False)
    password = models.CharField(max_length=20, null=False, blank=False)

class Inventario(models.Model):
    producto= models.CharField(max_length=10, null=False, blank=False)
    cantidad= models.IntegerField(null=False, blank=False)
    reutilizable= models.CharField(max_length=10, null=False, blank=False)
    bodega= models.CharField(max_length=10, null=False, blank=False)



class Pedido(models.Model):
    descripccion = models.CharField(max_length=200, null=False, blank=False)
    Proyecto = models.CharField(max_length=20, null=False, blank=False)
    idCliente = models.IntegerField( null=False, blank=False)
    cotizacion = models.CharField(max_length=10, null=False, blank=False)
    direccion = models.CharField(max_length=10, null=False, blank=False)



class Estado(models.Model):
    idProducto = models.IntegerField()
    idCliente = models.IntegerField()
    direccion = models.CharField(max_length=10)
