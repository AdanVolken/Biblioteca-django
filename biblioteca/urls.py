from django.contrib import admin
from django.urls import path

from .views import (
    home,
    biblioteca,
    mi_libro,
    libro_id,
    registro,
    sesion,    
)


urlpatterns = [
    path('', home, name="home"),
    path('registro/', registro ,name="registro"),
    path('login/', sesion, name="login"),
    path('biblioteca/', biblioteca, name="biblioteca"),
    path('mi_libro/', mi_libro, name="mi_libro"),
    path('biblioteca/libro/<int:id>/', libro_id, name="libro_id"),
]
