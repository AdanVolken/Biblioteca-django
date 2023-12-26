from django.contrib import admin
from .models import Cliente,LibroCompra,Compra,Genero
# Register your models here.

admin.site.register(Cliente)
admin.site.register(LibroCompra)
admin.site.register(Compra)
admin.site.register(Genero)