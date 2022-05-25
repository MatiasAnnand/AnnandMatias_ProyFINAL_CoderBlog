from msilib.schema import ListView
from pyexpat import model
from sqlite3 import Cursor
from django.http import HttpResponse
from django.shortcuts import render
from Aplicacion.forms import BlogFormulario, ProfeFormulario, EstudFormulario, RegistroFormulario
from Aplicacion.models import Avatar, Blog, Estudiante, Profesor
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin  #No se pueden utilizar decoradores con Clases. Para Vista basada en Clases se usa Mixins
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout


# Vista para registrarse
def register(request):

    if request.method == 'POST':

        form = RegistroFormulario(request.POST)

        if form.is_valid():

            user=form.cleaned_data['username']
            form.save()

            return render(request, "Aplicacion/inicio.html", {'mensaje':"Usuario Creado"})

    else:

        form = RegistroFormulario()  # formulario de django que permite crear usuarios

    return render(request, "Aplicacion/registro.html", {'form':form})


# Vista para iniciar sesion
def login_request(request):
    
    if request.method == 'POST':

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario=form.cleaned_data.get('username')
            clave=form.cleaned_data.get('password')

            user=authenticate(username=usuario, password=clave)

            if user:

                login(request, user)

                return render(request, "Aplicacion/inicio.html", {'mensaje':f"Bienvenido {user}"})

        else:

            return render(request, "Aplicacion/inicio.html", {'mensaje':"¡Error. Datos incorrectos!"})

    else:

        form = AuthenticationForm()

    return render(request, "Aplicacion/login.html", {'form':form})


# Vista Pagina Principal
@login_required
def inicio(request):

    avatares = Avatar.objects.filter(user=request.user.id)
    imagen = avatares[0].imagen.url
    return render(request, "Aplicacion/inicio.html", {'url':imagen})

# Vista para agregar un profesor
def profesor(request):

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

    return render(request, "Aplicacion/Profesores/profesor.html", {"miFormulario": miFormulario})

# Vista para agregar un estudiante
def estudiante(request):

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

    return render(request, "Aplicacion/Estudiantes/estudiante.html", {"miFormulario": miFormulario})

# Vista para crear un Posteo del Blog
def blog(request):

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

    return render(request, "Aplicacion/Blog/blog.html", {"miFormulario": miFormulario})


# Vista para buscar un posteo en el Blog
def busquedaBlog(request):

    return render(request, "Aplicacion/Blog/busquedaBlog.html")

# Busqueda por el filtro del titulo de un blog.
def buscar(request):

    if request.GET['titulo']:

        titulo = request.GET['titulo']
        blog = Blog.objects.filter(titulo__icontains=titulo)

        return render(request, "Aplicacion/Blog/resultadosBusqueda.html", {"blog": blog, "titulo": titulo})

    else:

        respuesta = "No enviaste datos."

    return HttpResponse(respuesta)


def about(request):
    return render(request, 'Aplicacion/about.html')


# Vista para mostrar los Posteos del Blog usando Clases (login required Mixin).
class MuroBlog(LoginRequiredMixin, ListView):
    model = Blog
    template_name = "Aplicacion/Blog/listaBlogs.html"

# Vista para mostrar el detalle de los Blogs usando Clases (CRUD con Clases)
class BlogDetalle(DetailView):
    model = Blog
    template_name = "Aplicacion/Blog/blogDetalle.html"

# Vista para crear Blogs usando Clases (CRUD con Clases)
class BlogCreacion(CreateView):
    model = Blog
    success_url = "/Aplicacion/blog/lista"
    fields = ['titulo', 'subtitulo', 'contenido', 'autor']

# Vista para mostrar/ actualizar los BLogs usando Clases (CRUD con Clases)
class BlogUpdate(UpdateView):
    model = Blog
    success_url = "/Aplicacion/blog/lista"
    fields = ['titulo', 'subtitulo', 'contenido', 'autor']

class BlogDelete(DeleteView):
    model = Blog
    success_url = "/Aplicacion/blog/lista"


# Vista para mostrar el listado de Profesores usando Clases (login required Mixin).
class ProfesorList(LoginRequiredMixin, ListView):
    model = Profesor
    template_name = "Aplicacion/Profesores/listaProfesores.html"

# Vista para mostrar el detalle de los Profesores usando Clases (CRUD con Clases)
class ProfesorDetalle(DetailView):
    model = Profesor
    template_name = "Aplicacion/Profesores/profesorDetalle.html"

# Vista para agregar Profesores usando Clases (CRUD con Clases)
class ProfesorCreacion(CreateView):
    model = Profesor
    success_url = "/Aplicacion/profesor/lista"
    fields = ['nombre', 'apellido', 'email', 'comision']

# Vista para mostrar/ actualizar los Profesores usando Clases (CRUD con Clases)
class ProfesorUpdate(UpdateView):
    model = Profesor
    success_url = "/Aplicacion/profesor/lista"
    fields = ['nombre', 'apellido', 'email', 'comision']

# Eliminar Profesores
class ProfesorDelete(DeleteView):
    model = Profesor
    success_url = "/Aplicacion/estudiante/lista"


# Vista para mostrar el listado de Estudiantes usando Clases (login required Mixin).
class EstudianteList(LoginRequiredMixin, ListView):
    model = Estudiante
    template_name = "Aplicacion/Estudiantes/listaEstudiantes.html"

# Vista para mostrar el detalle de los Estudiantes usando Clases (CRUD con Clases)
class EstudianteDetalle(DetailView):
    model = Estudiante
    template_name = "Aplicacion/Estudiantes/estudianteDetalle.html"

# Vista para agregar Estudiantes usando Clases (CRUD con Clases)
class EstudianteCreacion(CreateView):
    model = Estudiante
    success_url = "/Aplicacion/estudiante/lista"
    fields = ['nombre', 'apellido', 'email', 'comision']

# Vista para mostrar/ actualizar los Estudiantes usando Clases (CRUD con Clases)
class EstudianteUpdate(UpdateView):
    model = Estudiante
    success_url = "/Aplicacion/estudiante/lista"
    fields = ['nombre', 'apellido', 'email', 'comision']

# Eliminar Estudiantes
class EstudianteDelete(DeleteView):
    model = Estudiante
    success_url = "/Aplicacion/estudiante/lista"