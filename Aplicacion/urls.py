from django.urls import path
from Aplicacion import views

urlpatterns = [
    path('profesores/', views.profesor, name='Profesores'),
    path('estudiantes/', views.estudiante, name='Estudiantes'),
    path('blog/', views.blog, name='Blog'),
    path('', views.inicio, name='Inicio'),
    path('profeFormulario/', views.profeFormulario, name="ProfeFormulario"),
    path('estudFormulario/', views.estudFormulario, name="EstudFormulario"),
    path('blogFormulario/', views.blogFormulario, name="BlogFormulario"),
    path('busquedaBlog/', views.busquedaBlog, name="BusquedaBlog"),
    path('buscar/', views.buscar),
]