from django.db import models

# Create your models here.
class Libro(models.Model):
    nombre = models.CharField(max_length=15)
    archivo = models.FileField(upload_to='archivos_pdf/')

    def __str__(self):
        return self.nombre