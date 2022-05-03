from django.urls import path
from Aplicacion import views

urlpatterns = [
    path('profesores/', views.profesor),
    path('estudiantes/', views.estudiante),
    path('blog/', views.blog),
    path('', views.inicio),
]