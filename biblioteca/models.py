
from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

class Genero(models.Model):
    genero = models.CharField(max_length=50)

    def __str__(self):
        return self.genero

class LibroCompra(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    editorial = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    portada = models.ImageField(upload_to="portada/",blank=True, null = True)
    resumen = models.TextField(blank=True)
    genero = models.ManyToManyField(Genero)

    def __str__(self):
        return self.titulo

class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    libros_comprados = models.ManyToManyField(LibroCompra, through='Compra') 


    def __str__(self):
        return self.usuario.username

class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    libro = models.ForeignKey(LibroCompra, on_delete=models.CASCADE)
    descargado = models.BooleanField(default=False)
    fecha_compra = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente} compró {self.libro}"
    