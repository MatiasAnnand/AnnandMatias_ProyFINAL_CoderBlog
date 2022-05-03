from django import forms


class ProfeFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    comision = forms.IntegerField()


class EstudFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    comision = forms.IntegerField()


class BlogFormulario(forms.Form):

    titulo = forms.CharField()
    subtitulo = forms.CharField()
    contenido = forms.CharField()
    autor = forms.CharField()