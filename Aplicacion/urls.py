from django.urls import path
from Aplicacion import views

urlpatterns = [
    path('profesores/', views.profesor, name='Profesores'),
    path('estudiantes/', views.estudiante, name='Estudiantes'),
    path('blog/', views.blog, name='Blog'),
    path('', views.inicio, name='Inicio'),
    path('busquedaBlog/', views.busquedaBlog, name="BusquedaBlog"),
    path('buscar/', views.buscar),
]