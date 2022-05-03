from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField()
    comision = models.IntegerField()

    def __str__(self):
        txt="{0} , {1}"
        return txt.format(self.nombre, self.apellido)

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "profesores"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    email = models.EmailField()
    comision = models.IntegerField()

    def __str__(self):
        txt="{0} , {1}"
        return txt.format(self.nombre, self.apellido)

class Blog(models.Model):
    titulo = models.CharField(max_length=300)
    subtitulo = models.CharField(max_length=300)
    contenido = models.TextField()
    autor = models.CharField(max_length=300)

    def __str__(self):
        txt="{0} - {1}"
        return txt.format(self.titulo, self.autor)
