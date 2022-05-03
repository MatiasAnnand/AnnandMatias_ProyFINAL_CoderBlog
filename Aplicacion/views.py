from django.http import HttpResponse
from django.shortcuts import render
from Aplicacion.models import Profesor


def profesor(request):

    return render(request, "Aplicacion/profesor.html")


def estudiante(request):

    return render(request,"Aplicacion/estudiante.html")


def blog(request):

    return render(request, "Aplicacion/blog.html")


def inicio(request):

    return render(request, "Aplicacion/inicio.html")