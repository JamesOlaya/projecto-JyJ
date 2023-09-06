from django.db import models

class Usuario(models.Model):
    correo = models.CharField(max_length=50)
    nombre= models.CharField (max_length=30)
    Usuario= models.CharField(max_length=30)
    password= models.CharField(max_length=20)
    telefono= models.IntegerField()


class Encargado(models.Model):
    usuario = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Cliente(models.Model):
    usuario = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Inventario(models.Model):
    producto= models.CharField(max_length=10)
    cantidad= models.IntegerField()
    reutilizable= models.CharField(max_length=10)
    bodega= models.CharField(max_length=10)



class Pedido(models.Model):
    descripccion = models.CharField(max_length=200)
    Proyecto = models.CharField(max_length=20)
    idCliente = models.IntegerField()
    cotizacion = models.CharField(max_length=10)
    direccion = models.CharField(max_length=10)



class Estado(models.Model):
    idProducto = models.IntegerField()
    idCliente = models.IntegerField()
    direccion = models.CharField(max_length=10)
