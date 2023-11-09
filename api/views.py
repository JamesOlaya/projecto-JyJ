from django.shortcuts import render,redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import create_user,create_producto
import json
from .models import Usuario , Pedido,Producto
from django.contrib import messages 



def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')
    else:
        usuarios = list (Usuario.objects.all())

        usuario= request.POST['usuario']
        password =request.POST['Contraseña']

        
        for user in usuarios:
            if user.estatus == 'admin':
                if usuario == user.usuario and password == user.password:
                    return redirect('administrador')
                
            elif user.estatus == 'cliente':
                if usuario == user.usuario and password == user.password:
                    return redirect('cliente')
            else:
                messages.add_message(request=request, level=messages.SUCCESS, message='El usuario y/o la contraseña no son correctos, por favor vuélvalo a intentar.')
                return redirect('login')
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
        if nombre != '' and usuario != '' and correo != '' and telefono != '' and password != '':
            Usuario.objects.create(nombre=nombre,usuario=usuario,correo=correo,telefono=telefono,password=password)
            
            return redirect('/login')
        return redirect('/occount')


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
    
