from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField


#Clase para el posteo en Blog
class Posts(models.Model):
    #id = models.AutoField(primary_key=True)
    titulo=models.CharField(max_length=60)
    equipo=models.CharField(max_length=280)
    posteo=RichTextField()
    #Caratula de Inicio
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(upload_to='thumbnail/', null=True, blank=True)
    
    class Meta: 
        ordering = ["-creado"]
        
    def __str__(self):
        return f'{self.titulo} - {self.autor} de fecha {self.creado.day}/{self.creado.month}/{self.creado.day} a las {self.creado.hour}:{self.creado.minute}:{self.creado.second}'

class thumbnail(models.Model):
    posteothumb= models.ForeignKey(Posts, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='thumbnail/', null=True, blank=True)
    