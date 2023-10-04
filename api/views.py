from django.shortcuts import render,redirect
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .forms import create_user,create_producto
import json
from .models import Usuario, Cliente, Pedido,Producto,Encargado
from django.contrib import messages 



def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')
    else:
        clientes = list (Usuario.objects.all())
        administradores = list (Encargado.objects.all())
        usuario= request.POST['usuario']
        password =request.POST['Contraseña']
        ad= 'si'
        cl= 'si'
        
        for administrador in administradores:
            if usuario == administrador.usuario  :
                p_usuario = False
                p_password = False    
                if usuario == administrador.usuario:
                    p_usuario = True
                if password == administrador.password:
                    p_password = True

                if p_usuario == True and p_password == True:
                    messages.add_message(request=request, level=messages.SUCCESS, message='El usuario no puede ingresar al apartado de administrador.') 
                else:
                    messages.add_message(request=request, level=messages.SUCCESS, message='El usuario y/o la contraseña no son correctos, por favor vuélvalo a intentar.')
                    return redirect('login')
            else:
                ad = 'no'


        for cliente in clientes: 
            if usuario == cliente.usuario:  
                p_usuario = False
                p_password = False    
                if usuario == cliente.usuario:
                    p_usuario = True
                if password == cliente.password:
                    p_password = True
                if p_usuario == True and p_password == True and password != '' and usuario != '':
                    return redirect('cliente')
                else:
                    messages.add_message(request=request, level=messages.SUCCESS, message='El usuario y/o la contraseña no son correctos, por favor vuélvalo a intentar.')
                    return redirect('login')
            else:
                cl = 'no'
        if cl == 'no' and ad == 'no':
             messages.add_message(request=request, level=messages.SUCCESS, message='No se ha encontrado el usuario en la base de datos   .')

    return redirect('login')

            


def create_account(requst):
    if requst.method == 'GET':
        return render(requst, 'create_account/create_account.html',{
            'form': create_user,
        })
    else:
        nombre = requst.POST['nombre']
        usuario = requst.POST['usuario']
        correo = requst.POST['correo']
        telefono = requst.POST['telefono']
        password = requst.POST['contraseña']

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
    
