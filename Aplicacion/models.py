from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

class Profesor(models.Model):

    def __str__(self): # Permite mostrar la info mejor en el admin de la app
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} - Comision: {self.comision}"

    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField()
    comision = models.IntegerField()

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "profesores"

class Estudiante(models.Model):

    def __str__(self): # Permite mostrar la info mejor en el admin de la app
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email} - Comision: {self.comision}"

    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField()
    comision = models.IntegerField()

class Blog(models.Model):

    def __str__(self): # Permite mostrar la info mejor en el admin de la app
        return f"Titulo: {self.titulo} - Subtitulo: {self.subtitulo} - Contenido: {self.contenido} - Autor: {self.autor}"

    titulo = models.CharField(max_length=300)
    subtitulo = models.CharField(max_length=300)
    contenido = models.TextField()
    autor = models.CharField(max_length=300)

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to = 'avatares', null = True, blank = True)

    class Meta:
        verbose_name = "Avatar"
        verbose_name_plural = "Avatares"