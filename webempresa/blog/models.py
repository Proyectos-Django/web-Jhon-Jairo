from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User # Contienen todos los usuarios almacenados en el administrador

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["-created"]
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    content = models.TextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha de publicación', default=now) # tiempo hora zona horaria actual
    image = models.ImageField(verbose_name='Imagen', upload_to='blog', null=True, blank=True) # para decirle al usuario si coloque o no la imagen
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)# si se elimina un autor se elimina en todo lo que este relacionado
    categories = models.ManyToManyField(Category, verbose_name= 'Categorías', related_name='get_posts')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ["-created"]
    
    def __str__(self):
        return self.title 

