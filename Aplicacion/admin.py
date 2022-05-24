from django.contrib import admin
from .models import Avatar, Profesor, Estudiante, Blog
# el * tmb puede importar todos los modelos

admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Blog)
admin.site.register(Avatar)
