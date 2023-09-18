from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario,Encargado,Cliente,Inventario,Pedido,Estado

class create_user(UserCreationForm):
    correo = forms.CharField(max_length=50)
    nombre= forms.CharField (max_length=30)
    Usuario= forms.CharField(max_length=30)
    password= forms.CharField(max_length=20)
    telefono= forms.IntegerField()

class create_encargado(forms.Form):
    usuario = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)

class create_cliente(forms.Form):
    usuario = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)

class crear_pedido(forms.Form):
    descripccion = forms.CharField(max_length=200)
    Proyecto = forms.CharField(max_length=20)
    idCliente = forms.IntegerField()
    cotizacion = forms.CharField(max_length=10)
    direccion = forms.CharField(max_length=10)

