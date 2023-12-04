from django.shortcuts import render,redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import DeleteView
from .forms import create_user,create_material
import json
from .models import Usuario ,Pedido,Producto,Material
from django.contrib import messages 
from django.views import View



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
        if nombre != '' and usuario != '' and correo != '' and telefono != '' and password != '':
            Usuario.objects.create(nombre=nombre,usuario=usuario,correo=correo,telefono=telefono,password=password)
            
            return redirect('/login')
        return redirect('/occount')

def administrador(request):
    if request.method == 'GET':
        datos = Material.objects.all()
        
        return render(request, 'administrador/administrador.html',{
            'form': create_material,
            'datos': datos
        })
    elif request.method == 'POST':
        nombreM = request.POST['product-name']
        descripcionM = request.POST['product-description']
        precioM = request.POST['product-price']
        cantidadM = request.POST['product-quantity']
        print(nombreM, descripcionM, precioM, cantidadM)
        if nombreM != '' and descripcionM != '' and precioM != '' and cantidadM != '':
            Material.objects.create(nombreM=nombreM, descripcionM=descripcionM, precioM=precioM, cantidadM=cantidadM)
            return redirect('/admins')
        print('si se guardo')
        return redirect('/admins')
    elif request == 'PUT':
        pass
    else:
        datos = Material.objects.all()
        print(datos.id)
        material = list(Material.objects.filter(id=id).values())
        if len(material) > 0:
            Material.objects.filter(id=id).delete()
            return redirect('/admins')




def cliente(request):
    dato = 'El valor de la cotizacion de una:'
    if request.method == 'GET':
        return render(request, 'cliente/cliente.html')  
    else:
        valor = 0
        valor2 = 0
        desperdicios = 15
        select = request.POST['select']
        materiales = list(Material.objects.all())
        
  
        if (select == 'Puertas' ):
            material = request.POST['materialP']
            tipo = request.POST['tipoP']
            marco = request.POST['marcoP']
            manija = request.POST['manijaP']
            altura = float(request.POST['alturaP'])
            ancho = float(request.POST['anchoP'])

            if (material == 'vidrioS'):
                for data in materiales:
                    if data.nombreM == 'vidrios con control solar':
                        material = 'vidrios con control solar'
                        valor = data.precioM
            elif (material == 'vidrioE'):
                for data in materiales:
                    if data.nombreM == 'vidrios bajo emisivos':
                        material = 'vidrios bajo emisivos'
                        valor = data.precioM
            elif (material == 'vidrioT'):
                for data in materiales:
                    if data.nombreM == 'vidrio templado':
                        material = 'vidrio templado'
                        valor = data.precioM            
            elif (material == 'vidrioD'):
                for data in materiales:
                    if data.nombreM == 'vidrios con doble acristalamiento':
                        material = 'vidrios con doble acristalamiento'
                        valor = data.precioM
            elif (material == 'vidrioL'):
                for data in materiales:
                    if data.nombreM == 'Vidrio laminado':
                        material = 'Vidrio laminado'
                        valor = data.precioM
            elif (material == 'vidrioF'):
                for data in materiales:
                    if data.nombreM == 'vidrio flotado':
                        material = 'vidrio flotado'
                        valor = data.precioM                
            if (tipo == 'sencilla'):
                valor2 = 1
            elif(tipo == 'sencillaC'):
                valor2 = 1.05
            elif(tipo == 'sencillaD'):
                valor2 = 1.10
                
            neto= ((altura * ancho) * valor) * valor2
            procentaje = neto/ desperdicios
            cotizacion = neto + procentaje
            print(cotizacion)
            return render(request, 'cliente/cliente.html',{
            'datos': dato,
            'valor': round(cotizacion),
            'pedido': select + ' de ' + material + ' con marco de '+ marco + ' con manijas ' + manija + ' es de:'
        })            
        elif(select == 'Ventanas'):
            material = request.POST['materialV']
            tipo = request.POST['tipoV']
            altura = float(request.POST['alturaV'])
            ancho = float(request.POST['anchoV'])

            if (material == 'vidrioS'):
                for data in materiales:
                    if data.nombreM == 'vidrios con control solar':
                        valor = data.precioM
            elif (material == 'vidrioE'):
                for data in materiales:
                    if data.nombreM == 'vidrios bajo emisivos':
                        valor = data.precioM
            elif (material == 'vidrioT'):
                for data in materiales:
                    if data.nombreM == 'vidrio templado':
                        valor = data.precioM            
            elif (material == 'vidrioD'):
                for data in materiales:
                    if data.nombreM == 'vidrios con doble acristalamiento':
                        valor = data.precioM
            elif (material == 'vidrioL'):
                for data in materiales:
                    if data.nombreM == 'Vidrio laminado':
                        valor = data.precioM
            elif (material == 'vidrioF'):
                for data in materiales:
                    if data.nombreM == 'vidrio flotado':
                        valor = data.precioM                
            if (tipo == 'sencilla'):
                valor2 = 1
            elif(tipo == 'doble'):
                valor2 = 1.05
            elif(tipo == 'corredizaD'):
                valor2 = 1.10
                
            neto= ((altura * ancho) * valor) * valor2
            procentaje = neto/ desperdicios
            cotizacion = neto + procentaje
            print(cotizacion)
            return render(request, 'cliente/cliente.html',{
            'datos': dato,
            'valor': round(cotizacion)})
        elif(select == 'Cerramientos de Piscinas'):
            material = request.POST['materialC']
            tipo = request.POST['tipoC']
            altura = float(request.POST['alturaC'])
            area = float(request.POST['areaC'])
            distancia = float(request.POST['distaciaC'])


            if (material == 'vidrioS'):
                for data in materiales:
                    if data.nombreM == 'vidrios con control solar':
                        valor = data.precioM
            elif (material == 'vidrioE'):
                for data in materiales:
                    if data.nombreM == 'vidrios bajo emisivos':
                        valor = data.precioM
            elif (material == 'vidrioT'):
                for data in materiales:
                    if data.nombreM == 'vidrio templado':
                        valor = data.precioM            
            elif (material == 'vidrioD'):
                for data in materiales:
                    if data.nombreM == 'vidrios con doble acristalamiento':
                        valor = data.precioM
            elif (material == 'vidrioL'):
                for data in materiales:
                    if data.nombreM == 'Vidrio laminado':
                        valor = data.precioM
            elif (material == 'vidrioF'):
                for data in materiales:
                    if data.nombreM == 'vidrio flotado':
                        valor = data.precioM                
            if (tipo == 'Aluminio'):
                valor2 = 1
            elif(tipo == 'Acero'):
                valor2 = 1.05
                
            neto= ((altura * (area + distancia)) * valor) * valor2
            procentaje = neto/ desperdicios
            cotizacion = neto + procentaje
            print(cotizacion)
            return render(request, 'cliente/cliente.html',{
            'datos': dato,
            'valor': round(cotizacion)})
        elif(select == 'Divisiones de ducha'):
            material = request.POST['materialD']
            tipo = request.POST['tipoD']
            altura = float(request.POST['alturaD'])
            ancho = float(request.POST['anchoD'])

            if (material == 'vidrioS'):
                for data in materiales:
                    if data.nombreM == 'vidrios con control solar':
                        valor = data.precioM
            elif (material == 'vidrioE'):
                for data in materiales:
                    if data.nombreM == 'vidrios bajo emisivos':
                        valor = data.precioM
            elif (material == 'vidrioT'):
                for data in materiales:
                    if data.nombreM == 'vidrio templado':
                        valor = data.precioM            
            elif (material == 'vidrioD'):
                for data in materiales:
                    if data.nombreM == 'vidrios con doble acristalamiento':
                        valor = data.precioM
            elif (material == 'vidrioL'):
                for data in materiales:
                    if data.nombreM == 'Vidrio laminado':
                        valor = data.precioM
            elif (material == 'vidrioF'):
                for data in materiales:
                    if data.nombreM == 'vidrio flotado':
                        valor = data.precioM                
            if (tipo == 'Cubiciulo'):
                valor2 = 1.20
            elif(tipo == 'LaL'):
                valor2 = 1.10 
            neto= ((altura * ancho) * valor) * valor2
            procentaje = neto/ desperdicios
            cotizacion = neto + procentaje
            print(cotizacion)
            return render(request, 'cliente/cliente.html',{
            'datos': dato,
            'valor': round(cotizacion)
        })            
        elif(select == 'Balcones en vidrio'):
            material = request.POST['materialB']
            tipo = request.POST['tipoB']
            altura = float(request.POST['alturaB'])
            ancho = float(request.POST['anchoB'])
            cantidad = float(request.POST['cantidadB'])

            if (material == 'vidrioS'):
                for data in materiales:
                    if data.nombreM == 'vidrios con control solar':
                        valor = data.precioM
            elif (material == 'vidrioE'):
                for data in materiales:
                    if data.nombreM == 'vidrios bajo emisivos':
                        valor = data.precioM
            elif (material == 'vidrioT'):
                for data in materiales:
                    if data.nombreM == 'vidrio templado':
                        valor = data.precioM            
            elif (material == 'vidrioD'):
                for data in materiales:
                    if data.nombreM == 'vidrios con doble acristalamiento':
                        valor = data.precioM
            elif (material == 'vidrioL'):
                for data in materiales:
                    if data.nombreM == 'Vidrio laminado':
                        valor = data.precioM
            elif (material == 'vidrioF'):
                for data in materiales:
                    if data.nombreM == 'vidrio flotado':
                        valor = data.precioM                
            if (tipo == 'BM'):
                valor2 = 50000
            elif(tipo == 'AVF'):
                valor2 = 60000
            elif(tipo == 'HA'):
                valor2 = 50000  
            division= ((altura * ancho) * valor) / cantidad
            neto =(((altura * ancho)* valor2)+ ((altura * ancho) * valor)) - division
            procentaje = neto/ desperdicios
            cotizacion = neto + procentaje
            print(cotizacion)
            return render(request, 'cliente/cliente.html',{
            'datos': dato,
            'valor': round(cotizacion)})
        elif(select == 'Fachadas en vidrio'):
            material = request.POST['materialF']
            tipo = request.POST['tipoF']
            altura = float(request.POST['alturaF'])
            ancho = float(request.POST['anchoF'])
            cantidad = float(request.POST['cantidadF'])

            if (material == 'vidrioS'):
                for data in materiales:
                    if data.nombreM == 'vidrios con control solar':
                        valor = data.precioM
            elif (material == 'vidrioE'):
                for data in materiales:
                    if data.nombreM == 'vidrios bajo emisivos':
                        valor = data.precioM
            elif (material == 'vidrioT'):
                for data in materiales:
                    if data.nombreM == 'vidrio templado':
                        valor = data.precioM            
            elif (material == 'vidrioD'):
                for data in materiales:
                    if data.nombreM == 'vidrios con doble acristalamiento':
                        valor = data.precioM
            elif (material == 'vidrioL'):
                for data in materiales:
                    if data.nombreM == 'Vidrio laminado':
                        valor = data.precioM
            elif (material == 'vidrioF'):
                for data in materiales:
                    if data.nombreM == 'vidrio flotado':
                        valor = data.precioM                
            if (tipo == 'Aluminio'):
                valor2 = 1000
            elif(tipo == 'Acero'):
                valor2 = 1000
 
            division= ((altura * ancho) * valor) / cantidad
            neto =(((altura * ancho)* valor2)+ ((altura * ancho) * valor)) - division
            procentaje = neto/ desperdicios
            cotizacion = neto + procentaje
            print(cotizacion)
            return render(request, 'cliente/cliente.html',{
            'datos': dato,
            'valor': round(cotizacion)})
        elif(select == 'Techos en policarbonato'):
            material = request.POST['materialV']
            tipo = request.POST['tipoV']
            altura = float(request.POST['alturaV'])
            ancho = float(request.POST['anchoV'])

            if (material == 'vidrioS'):
                for data in materiales:
                    if data.nombreM == 'vidrios con control solar':
                        valor = data.precioM
            elif (material == 'vidrioE'):
                for data in materiales:
                    if data.nombreM == 'vidrios bajo emisivos':
                        valor = data.precioM
            elif (material == 'vidrioT'):
                for data in materiales:
                    if data.nombreM == 'vidrio templado':
                        valor = data.precioM            
            elif (material == 'vidrioD'):
                for data in materiales:
                    if data.nombreM == 'vidrios con doble acristalamiento':
                        valor = data.precioM
            elif (material == 'vidrioL'):
                for data in materiales:
                    if data.nombreM == 'Vidrio laminado':
                        valor = data.precioM
            elif (material == 'vidrioF'):
                for data in materiales:
                    if data.nombreM == 'vidrio flotado':
                        valor = data.precioM                
            if (tipo == 'sencilla'):
                valor2 = 1
            elif(tipo == 'doble'):
                valor2 = 1.05
            elif(tipo == 'corredizaD'):
                valor2 = 1.10
                
            neto= ((altura * ancho) * valor) * valor2
            procentaje = neto/ desperdicios
            cotizacion = neto + procentaje
            print(cotizacion)
            return render(request, 'cliente/cliente.html',{
            'datos': dato,
            'valor': round(cotizacion)})


def usuario(request):
    return render(request, 'usuario/usuario.html')

