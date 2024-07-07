from django.db import models

# Create your models here.
class Receta(models.Model):
    """Definimos la clase Receta"""
    title = models.CharField(max_length=200, verbose_name="Título")
    ingredient = models.TextField(verbose_name= "Ingredientes")
    description=models.TextField(verbose_name= "Descripción")
    image=models.ImageField(verbose_name= "Foto", upload_to="recipes")
    created=models.DateTimeField(auto_now_add=True, verbose_name= "Creado")
    updated=models.DateTimeField(auto_now=True, verbose_name= "Actualizado")

    def __str__(self):
        return self.title
    