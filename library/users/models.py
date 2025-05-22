from django.db import models
from django.contrib.auth.models import User 
from libros.models import Libro
# Create your models here.
    
class registro(models.Model):
    user = models.ForeignKey(User, null = True, on_delete= models.CASCADE)
    telefono = models.CharField(max_length=20, default='')
    direccion = models.CharField(max_length=255, default='')
    edad = models.IntegerField(null=True, blank=True)


class Author(models.Model):
    datos = models.ForeignKey(User, related_name="info", on_delete=models.CASCADE)
    alias = models.CharField(max_length=100)
    date_start= models.DateTimeField()
    cantidad_libros =models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.alias

class AuthorLibros(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    autor = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.autor.alias} - {self.libro.titulo}"
    

