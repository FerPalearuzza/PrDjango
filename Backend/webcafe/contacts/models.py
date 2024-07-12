from django.db import models

# Create your models here.

class Contacto(models.Model):
    """Definimos la clase contacto"""
    fullname = models.CharField(max_length=200, verbose_name="Nombre y apellido")
    email = models.EmailField(verbose_name= "Correo electronico")
    consulttype=models.CharField(max_length=60, verbose_name= "Tipo de consulta")
    comments=models.TextField(verbose_name= "Mensaje")
    bulletin = models.BooleanField(verbose_name="Suscripto")
    created=models.DateTimeField(auto_now_add=True, verbose_name= "Creado")
    updated=models.DateTimeField(auto_now=True, verbose_name= "Actualizado")
    
    def __str__(self):
        return self.email