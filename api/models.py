from django.db import models

class Usuario(models.Model):
    correo = models.CharField(max_length=50, null=False, blank=False)
    nombre= models.CharField (max_length=30, null=False, blank=False)
    usuario= models.CharField(max_length=30, null=False, blank=False)
    password= models.CharField(max_length=20, null=False, blank=False)
    telefono= models.BigIntegerField( null=False, blank=False)
    estatus = models.CharField(max_length=8, default='cliente', null=False, blank=False)


class Material(models.Model):
    nombreM=models.CharField(max_length=100, null=False, blank=False)
    precioM=models.BigIntegerField( null=False, blank=False)
    descripcionM=models.CharField(max_length=300, default='none')
    cantidadM = models.BigIntegerField( null= False, blank=False, default=1)

class Inventario(models.Model):
    producto= models.CharField(max_length=10, null=False, blank=False)
    cantidad= models.IntegerField(null=False, blank=False)
    reutilizable= models.CharField(max_length=10, null=False, blank=False)
    bodega= models.CharField(max_length=10, null=False, blank=False)
    
class Producto(models.Model):
    nombreP=models.CharField(max_length=30,null=False, blank=False)
    precioP=models.BigIntegerField(null=False, blank=False)

class Pedido(models.Model):
    descripccion = models.CharField(max_length=200, null=False, blank=False)
    Proyecto = models.CharField(max_length=20, null=False, blank=False)
    idCliente = models.ForeignKey(Usuario,on_delete=models.CASCADE )
    cotizacion = models.CharField(max_length=10, null=False, blank=False)
    direccion = models.CharField(max_length=10, null=False, blank=False)

class Estado(models.Model):
    idProducto = models.ForeignKey(Producto,on_delete=models.CASCADE )
    idCliente = models.ForeignKey(Usuario,on_delete=models.CASCADE )
    direccion = models.CharField(max_length=10)


