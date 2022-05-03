from django.http import HttpResponse
from django.shortcuts import render
from Aplicacion.models import Profesor


def profesor(self):

    profe1 = Profesor(nombre="Pepe", apellido="Pascual",
                      email="peppas@hotmail.com", comision="20201")

    profe1.save()

    documento = f"El profesor es {profe1.nombre} de apellido {profe1.apellido}, de la comision {profe1.comision}. Mail: {profe1.email}."

    return HttpResponse(documento)
