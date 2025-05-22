from django.db import models

# Create your models here.

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    author = models.ForeignKey('users.Author',related_name="info", on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    publicado = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.titulo} - {self.author.datos}" 
    

