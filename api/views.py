from django.shortcuts import render,redirect
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .forms import  create_user,create_producto ,crear_pedido
import json
from .models import Usuario, Encargado, Cliente, Pedido, Producto



def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')
    else:
        clientes = list (Usuario.objects.all())
        usuario= request.POST['usuario']
        password =request.POST['Contraseña']
        ver_usuario = False
        ver_password = False

        for cliente in clientes:
            if cliente.usuario == usuario and ver_usuario == False:
                ver_usuario = True
            if cliente.password == password and ver_password == False:
                ver_password = True
        if ver_usuario == True and ver_password == True:
            return redirect('index')
        else:
            return redirect('occount')

def create_account(request):
    if request.method == 'GET':
        return render(request, 'create_account/create_account.html',{
            'form': create_user,
        })
    else:
        nombre = request.POST['nombre']
        usuario = request.POST['usuario']
        correo = request.POST['correo']
        telefono = request.POST['telefono']
        password = request.POST['contraseña']

        Cliente.objects.create(usuario=usuario, password=password)
        Usuario.objects.create(nombre=nombre,usuario=usuario,correo=correo,telefono=telefono,password=password)
        return redirect('/login')
    
def administrador(request):
    return render(request, 'administrador/administrador.html')

def cliente(request):
    return render(request, 'cliente/cliente.html')

def usuario(request):
    return render(request, 'usuario/usuario.html')

def cambiar_precios(request):
    if request.method == 'PUT':
        id=request.PUT['id']
        productosP = list(Producto.objects.filter(id=id).values())
        if len(productosP) > 0:
            producto = Producto.objects.get(id=id)
            producto.predioP = request.PUT['precio']
            producto.save()

        
    else:
        return render(request, 'create_account/create_account.html',{
            'form': create_user,
        })
    
def create_product(request):
    if request.method == 'GET':
        return render(request, 'create_account/create_account.html',{
            'form': create_producto,
        })
    else:
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        

        Producto.objects.create(nombreP=nombre, precioP=precio)
        return redirect('/login')

def delete_material(request):
    if request.method == 'delete':
        id=request.PUT['id']
        materiales = list(Producto.objects.filter(id=id).values())
        if len(materiales) > 0:
            Producto.objects.filter(id=id).delete()
    else:
        return render(request, 'create_account/create_account.html',{
            'form': create_user,
        })