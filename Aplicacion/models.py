from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField()
    comision = models.IntegerField()


class Estudiante(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField()
    comision = models.IntegerField()

class Blog(models.Model):
    titulo = models.CharField(max_length=300)
    subtitulo = models.CharField(max_length=300)
    contenido = models.TextField()
    autor = models.CharField(max_length=300)
