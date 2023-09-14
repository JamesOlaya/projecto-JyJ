from django.shortcuts import render,redirect
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .forms import create_cliente, create_user, create_encargado,crear_pedido
import json
from .models import Usuario, Encargado, Cliente, Pedido


def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login/login.html')

def create_account(request):
   
    if request.method == 'GET':
        return render(request, 'create_account/create_account.html',{
            'form': create_user()
        })
    #else:
       # jd = json.loads(request.body)
        #if jd:
            #correo = jd['correo']
            
            #nombre= jd['nombre']
            #usuario= jd['usuario']
            #password= jd['password']
            #telefono= jd['telefono']
            #Usuario.objects.create(correo =correo, nombre=nombre, usuario=usuario, password=password, telefono=telefono)
        
    return redirect('/login')
    
# def message(request):
    render(request, {
        ''
    })
    return redirect('/login')
def inicio_sesion (request):
    pass 









