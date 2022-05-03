from sqlite3 import Cursor
from django.http import HttpResponse
from django.shortcuts import render
from Aplicacion.forms import BlogFormulario, ProfeFormulario, EstudFormulario
from Aplicacion.models import Blog, Estudiante, Profesor


def profesor(request):

    return render(request, "Aplicacion/profesor.html")


def estudiante(request):

    return render(request, "Aplicacion/estudiante.html")


def blog(request):

    return render(request, "Aplicacion/blog.html")


def inicio(request):

    return render(request, "Aplicacion/inicio.html")


def profeFormulario(request):

    if request.method == 'POST':

        miFormulario = ProfeFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            profesor = Profesor(
                nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], comision=informacion['comision'])

            profesor.save()

            return render(request, "Aplicacion/inicio.html")

    else:
        miFormulario = ProfeFormulario()

    return render(request, "Aplicacion/profeFormulario.html", {"miFormulario":miFormulario})


def estudFormulario(request):

    if request.method == 'POST':

        miFormulario = EstudFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            estudiante = Estudiante(
                nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], comision=informacion['comision'])

            estudiante.save()

            return render(request, "Aplicacion/inicio.html")

    else:
        miFormulario = EstudFormulario()

    return render(request, "Aplicacion/estudFormulario.html", {"miFormulario":miFormulario})


def blogFormulario(request):

    if request.method == 'POST':

        miFormulario = BlogFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            blog = Blog(
                titulo=informacion['titulo'], subtitulo=informacion['subtitulo'], autor=informacion['autor'])

            blog.save()

            return render(request, "Aplicacion/inicio.html")

    else:
        miFormulario = BlogFormulario()

    return render(request, "Aplicacion/blogFormulario.html", {"miFormulario":miFormulario})


def busquedaBlog(request):
    
    return render(request, "Aplicacion/busquedaBlog.html")

def buscar(request):

    if request.GET['titulo']:

        titulo = request.GET['titulo']
        blog = Blog.objects.filter(titulo__icontains=titulo)

        return render(request, "Aplicacion/resultadosBusqueda.html", {"blog":blog, "titulo":titulo})

    else:

        respuesta = "No enviaste datos."

    return HttpResponse(respuesta)
