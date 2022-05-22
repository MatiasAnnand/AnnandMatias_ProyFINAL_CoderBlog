from django.db import models

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
