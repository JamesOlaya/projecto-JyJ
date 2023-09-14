from django.contrib import admin
from .models import Usuario,Encargado,Estado,Cliente,Inventario,Pedido
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Encargado)
admin.site.register(Estado)
admin.site.register(Cliente)
admin.site.register(Inventario)
admin.site.register(Pedido)