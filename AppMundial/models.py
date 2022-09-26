from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Avatar(models.Model):
    # Vinculo con el usuario
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # Subcaperta avatares de media :)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"Imagen de: {self.user}"

#Clase para el posteo en Blog
class Posts(models.Model):
    id = models.AutoField(primary_key=True)
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
    image = models.ImageField(upload_to='thumbnail', null=True, blank=True)

    def __str__(self):
        return f'{self.titulo} - {self.autor} - {self.creado} '

class thumbnail(models.Model):
    articulothumb= models.ForeignKey(Posts, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='thumbnail', null=True, blank=True)