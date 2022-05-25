from django.urls import path, re_path
from Aplicacion import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('profesores/', views.profesor, name='Profesores'),  # URL para la vista por defecto creada en views.py
    path('estudiantes/', views.estudiante, name='Estudiantes'),  # URL para la vista por defecto creada en views.py
    path('blog/', views.blog, name='Blog'),  # URL para la vista por defecto creada en views.py
    path('', views.inicio, name='Inicio'),  # URL para la vista por defecto creada en views.py
    path('busquedaBlog/', views.busquedaBlog, name="BusquedaBlog"),
    path('buscar/', views.buscar),
    path('about', views.about, name='aboutMe'),

    path("blog/lista", views.MuroBlog.as_view(), name='ListBlogs'),
    re_path(r'^(?P<pk>\d+)$', views.BlogDetalle.as_view(), name='Detail'),
    re_path(r'^nuevob$', views.BlogCreacion.as_view(), name='Create'),
    re_path(r'^editarb/(?P<pk>\d+)$', views.BlogUpdate.as_view(), name='Edit'),
    re_path(r'^borrarb/(?P<pk>\d+)$', views.BlogDelete.as_view(), name='Delete'),

    path("profesor/lista", views.ProfesorList.as_view(), name='ListProfesores'),
    re_path(r'^(?P<pk>\d+)$', views.ProfesorDetalle.as_view(), name='TeacherDetail'),
    re_path(r'^nuevop$', views.ProfesorCreacion.as_view(), name='TeacherCreate'),
    re_path(r'^editarp/(?P<pk>\d+)$', views.ProfesorUpdate.as_view(), name='TeacherEdit'),
    re_path(r'^borrarp/(?P<pk>\d+)$', views.ProfesorDelete.as_view(), name='TeacherDelete'),

    path("estudiante/lista", views.EstudianteList.as_view(), name='ListEstudiantes'),
    re_path(r'^(?P<pk>\d+)$', views.EstudianteDetalle.as_view(), name='StudentDetail'),
    re_path(r'^nuevoe$', views.EstudianteCreacion.as_view(), name='StudentCreate'),
    re_path(r'^editare/(?P<pk>\d+)$', views.EstudianteUpdate.as_view(), name='StudentEdit'),
    re_path(r'^borrare/(?P<pk>\d+)$', views.EstudianteDelete.as_view(), name='StudentDelete'),

    path('login', views.login_request, name='Login'),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='Aplicacion/logout.html'), name='Logout'),
]