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
    if request.method == 'GET':
        datos = Material.objects.all()
        
        return render(request, 'administrador/administrador.html',{
            'form': create_material,
            'datos': datos
        })
    elif request == 'POST':
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
    dato = 'el valor de su cotizacion es de'
    if request.method == 'GET':
        return render(request, 'cliente/cliente.html')  
    else:
        valor = 0
        valor2 = 0
        desperdicios = 25
        select = request.POST['select']
        materiales = list(Material.objects.all())
        print(select)
        
  
        if (select == 'Puertas' ):

            

            material = request.POST['materialP']
            tipo = request.POST['tipoP']
            altura = float(request.POST['alturaP'])
            ancho = float(request.POST['anchoP'])

            if (material == 'vidrioS'):
                valor = materiales[0].precioM
                
            if (tipo == 'sencilla'):
                valor2 = 1
                
            neto= ((altura * ancho) * valor) * valor2
            procentaje = neto/ desperdicios
            cotizacion = neto + procentaje
            print(cotizacion)
            return render(request, 'cliente/cliente.html',{
            'datos': dato,
            'valor': cotizacion
        })            

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
        return render(request, 'administrador/administrador.html',{
            'form': create_material,
        })
    else:
        nombre = request.POST['material-name']
        precio = request.POST['material-price']
        cantidad = request.POST['material-cantidad']
        

        Material.objects.create(nombreM=nombre, precioM=precio , cantidadM = cantidad)
        return redirect('/admins')

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
    
#class ProductView(View):




#    @method_decorator(csrf_exempt)
#    def dispatch(self, request, *args, **kwargs):
#        return super().dispatch(request, *args, **kwargs)
    
#    def get(self, request,id=0):
        if (id>0):
            products=list(Producto.objects.filter(id=id).values())
            if len(products )>0:
                product=products[0]
                datos = {'message': "Success", 'product': product}
            else:
                datos = {'message': "products not found..."}
            return (datos)
        else:
            products=list(Producto.objects.values())
            if len(products )> 0:
                datos = {'message': "Success", 'products': products}
            else:
                datos = {'message': "products not found..."}
                
            return (datos)
        

#    def post(self, request):
        # print(request.body)
#        jd =json.loads(request.body)
        # print(jd)
#        Producto.objects.create(name=jd['name'], descripccion=jd['descripccion'], precio=jd['precio'], stock=jd['stock'])
#        datos = {'message': "Success"}
#        return (datos)

 #   def put(self, request, id):
        jd =json.loads(request.body)
        products=list(Producto.objects.filter(id=id).values())
        if len(products )>0:
            product = Producto.objects.get(id=id)
            product.name =jd['name']
            product.descripccion = jd['descripccion']
            product.precio =jd['precio']
            product.stock =jd['stock']
            product.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "product not found..."}
        return (datos)
    
#    def delete(self, request,id):
        products = list(Producto.objects.filter(id=id).values())
        if len(products) > 0:
            Producto.objects.filter(id=id).delete()
            datos = {'message': "Success"}

        else:
            datos = {'message': "product not found..."}
        return (datos)

        