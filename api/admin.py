from django.contrib import admin
from .models import Usuario,Estado,Inventario,Pedido,Material
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Estado)
admin.site.register(Inventario)
admin.site.register(Pedido)
admin.site.register(Material)