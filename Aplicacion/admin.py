from django.contrib import admin
from .models import Profesor, Estudiante, Blog

admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Blog)