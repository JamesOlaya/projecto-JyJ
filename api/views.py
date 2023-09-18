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
    if request.method == 'POST':
        form = create_user(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = create_user()
    return render(request, 'create_account/create_account.html', {'form': form})
    
def administrador(request):
    return render(request, 'administrador/administrador.html')

def cliente(request):
    return render(request, 'cliente/cliente.html')

def usuario(request):
    return render(request, 'usuario/usuario.html')









