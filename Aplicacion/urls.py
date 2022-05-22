from django.urls import path
from Aplicacion import views

urlpatterns = [
    path('profesores/', views.profesor, name='Profesores'),  # URL para la vista por defecto creada en views.py
    path('estudiantes/', views.estudiante, name='Estudiantes'),  # URL para la vista por defecto creada en views.py
    path('blog/', views.blog, name='Blog'),  # URL para la vista por defecto creada en views.py
    path('', views.inicio, name='Inicio'),  # URL para la vista por defecto creada en views.py
    path('busquedaBlog/', views.busquedaBlog, name="BusquedaBlog"),
    path('buscar/', views.buscar),

    path("blog/lista", views.MuroBlog.as_view(), name='ListBlogs'),
    path(r'^(?P<pk>\d+)$', views.BlogDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.BlogCreacion.as_view(), name='Create'),
    path(r'^editar/(?P<pk>\d+)$', views.BlogUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.BlogDelete.as_view(), name='Delete'),

    path("profesor/lista", views.ProfesorList.as_view(), name='ListProfesores'),
    path(r'^(?P<pk>\d+)$', views.ProfesorDetalle.as_view(), name='TeacherDetail'),
    path(r'^nuevo$', views.ProfesorCreacion.as_view(), name='TeacherCreate'),
    path(r'^editar/(?P<pk>\d+)$', views.ProfesorUpdate.as_view(), name='TeacherEdit'),
    path(r'^borrar/(?P<pk>\d+)$', views.ProfesorDelete.as_view(), name='TeacherDelete'),

    path("estudiante/lista", views.EstudianteList.as_view(), name='ListEstudiantes'),
    path(r'^(?P<pk>\d+)$', views.EstudianteDetalle.as_view(), name='StudentDetail'),
    path(r'^nuevo$', views.EstudianteCreacion.as_view(), name='StudentCreate'),
    path(r'^editar/(?P<pk>\d+)$', views.EstudianteUpdate.as_view(), name='StudentEdit'),
    path(r'^borrar/(?P<pk>\d+)$', views.EstudianteDelete.as_view(), name='StudentDelete'),
]