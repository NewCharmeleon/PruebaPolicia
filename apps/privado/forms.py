from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db import models
from apps.publico.models import *
from datetime import datetime
from .models import *
from tinymce.widgets import TinyMCE


CARGO = ((1 , 'Jefe de Policia'), (2, 'SubJefe de Policia'), (3, 'Secretario General'), (4, 'Director'), (5, 'Jefe de Area'), (6, 'SubJefe de Area'), (7, 'Jefe'), (8, 'SubJefe'),)
JERARQUIA = ((1 , 'Crio. General'), (2, 'Crio. Mayor'), (3, 'Crio. Inspector'), (4, 'Comisario'),(5, 'SubCrio.'),(6, 'Of. Principal'),(7, 'Of. Inspector.'),(8, 'Of. SubInsp.'),(9, 'Retirado'),(10, 'Retirado en servicio'),)
LUGAR = ((1 , 'Jefatura de Policia'), (2, 'Secretaria General'), (3, 'Direccion Seguridad'), (4, 'Direccion Recursos Humanos'),(5, 'Direccion Recursos Materiales'),(6, 'Direccion Policia Judicial'),)
TIPO = ((1 , 'Resistencia'), (2, 'Elongacion'),)
ZONA = ((0, 'Tren Superior'),(1, 'Zona Superior'),(2 , 'Tren Inferior'),)

class LoginForm(forms.Form):
	user = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control','placeholder':'Usuario'})))
	password = forms.CharField(widget=forms.PasswordInput(attrs=dict({'class':'form-control','placeholder':'ContraseÃ±a'})))



'''
class PublicacionFotoForm(ModelForm):
	imagen = forms.ImageField(required=False,widget=forms.FileInput(attrs=dict({'class':'form-control','id':'uploadImage1','type':'file','name':'images[1]','onchange':'previewImage(1);'})))
	
	class Meta:
		model = PublicacionFoto
		#fields = ['album', 'imagen']
		exclude = []
'''

class PublicacionForm(ModelForm):
	
	class Meta:
		model = Publicacion
		exclude = ['usuario']

	#TIPO = ((1 , 'articulo'), (2, 'video'),)

	tipo = forms.ChoiceField(choices = Publicacion.TIPO,required=True, widget=forms.RadioSelect(attrs=dict({})))
	jurisdiccion = forms.ChoiceField(choices = Publicacion.JURISDICCION,required=True, widget=forms.Select(attrs=dict({})))
	categoria = forms.ChoiceField(choices = Publicacion.CATEGORIA,required=True, widget=forms.Select(attrs=dict({})))
	titulo = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Titulo','required':'required', 'style':'text-align: left;'})))
	contenido = forms.CharField(required=True, widget=forms.Textarea(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Contenido','required':'required', 'style':'text-align:left'})))
	#contenido = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
	url = forms.URLField(max_length=200, required=False, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Ingrese Url','style':'text-align: left;'})))
	fuente = forms.CharField(required=False, max_length=150, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Ingrese la Fuente','style':'text-align: left;'})))
	imagen = forms.ImageField(required=False,widget=forms.FileInput(attrs=dict({'id':'uploadImage1', 'type':'file','name':'images[1]','onchange':'previewImage(1);'})))
	#class="form-control" id="uploadImage1" type="file" name="images[1]" onchange="previewImage(1);"
	#foto = forms.ForeignKey(Fotos, on_delete = 'CASCADE')
	intro = forms.CharField(required=False,widget=forms.TextInput(attrs=dict({'class':'form-control input-lg','placeholder':'Introduccion', 'style':'text-align: left;'})))



class AutoridadForm(ModelForm):

	class Meta:
		model = Autoridad
		exclude = ['usuario']
	
	#telefono_regex = RegexValidator(regex=r'^[(\d](?:(?:00)?549?)?0?(?:11|[2\d\d\d]\d\d\d)[)\d](?:(?=\d{0,2}15)\d{2})??([-\s]\d{7,9}).+$', message="El telefono debe tener formato: '+999999999'. Hasta 15 digitos es permitido.")
	#forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control'}), queryset= RefOcupacionEspecifica.objects.all()  )
	jerarquia = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-lg'})),queryset=Jerarquia.objects.all(),empty_label='Seleccione jerarquia')
	cargo = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-lg'})),queryset=Cargo.objects.all(),empty_label='Seleccione cargo')
	lugar = forms.ModelChoiceField(widget=forms.Select(attrs=dict({'class':'form-control input-lg'})),queryset = Lugar.objects.all(),empty_label='Seleccione dependencia')
	
	nombre = forms.CharField(required=True, max_length=20, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Nombre','required':'required', 'style':'text-align: left;'})))
	segundo_nombre = forms.CharField(required=False, max_length=20, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Segundo Nombre', 'style':'text-align: left;'})))
	apellido = forms.CharField(required=True, max_length=20, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Apellido','required':'required', 'style':'text-align: left;'})))
	imagen = forms.ImageField(required=True,widget=forms.FileInput(attrs=dict({'id':'imagen1','onchange':'revisarImagen(this,1);'})))
	direccion_laboral =  forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Direccion Laboral','required':'required', 'style':'text-align: left;'})))
	telefono_laboral = forms.CharField(required=True, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Telefono Laboral','required':'required', 'style':'text-align: left;'})))
	telefono = forms.CharField(required=True, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Telefono','required':'required', 'style':'text-align: left;'})))
	email = forms.EmailField(max_length=150, required=True, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Ingrese Email','style':'text-align: left;'})))
	trayectoria = forms.CharField(required=True, widget=forms.Textarea(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Trayectoria','required':'required', 'style':'text-align:left'})))
	
class CargoForm(ModelForm):
	
	descripcion = forms.CharField(required=True, max_length=50)
	
	class Meta:
		model = Cargo
		exclude = []

class JerarquiaForm(ModelForm):
		
	descripcion = forms.CharField(required=True, max_length=50)

	class Meta:
		model = Jerarquia
		exclude = []

class LugarForm(ModelForm):

	descripcion = forms.CharField(required=True, max_length=50)
	
	class Meta:
		model = Lugar
		exclude = []

class DependenciaForm(ModelForm):

	class Meta:
		model = Dependencia
		exclude = ['usuario']
	
	#JURISDICCION = ((0, 'Provincial'),(1, 'Jefatura de Policia'),(2 , 'Unidad Regional Comodoro Rivadavia'), (3, 'Unidad Regional Esquel'),(4, 'Unidad Regional Puerto Madryn'),(5, 'Unidad Regional Trelew'),)
	#FUNCION = ((0, 'Seguridad'),(1, 'Escuela'),)
	
	jurisdiccion = forms.ChoiceField(choices = Dependencia.JURISDICCION,required=True, widget=forms.Select(attrs=dict({})))
	funcion = forms.ChoiceField(choices = Dependencia.FUNCION,required=True, widget=forms.Select(attrs=dict({})))

	nombre = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Nombre','required':'required', 'style':'text-align: left;'})))
	direccion = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Direccion','required':'required', 'style':'text-align: left;'})))
	ciudad = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Ciudad','required':'required', 'style':'text-align: left;'})))
	telefono = forms.CharField(required=True, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Telefono','required':'required', 'style':'text-align: left;'})))
	email = forms.EmailField(max_length=150, required=False, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Ingrese Email','style':'text-align: left;'})))
	jefe = forms.CharField(required=False, max_length=50, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Jefe', 'style':'text-align: left;'})))
	subjefe = forms.CharField(required=False, max_length=50, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'SubJefe', 'style':'text-align: left;'})))
	ubicacion = forms.CharField(required=False, max_length=150, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Ubicacion', 'style':'text-align: left;'})))
	imagen = forms.ImageField(required=False,widget=forms.FileInput(attrs=dict({'id':'imagen1','onchange':'revisarImagen(this,1);'})))
		
	#phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
	usuario = models.ForeignKey(User, on_delete = 'CASCADE', default=User)

class EjercicioForm(ModelForm):
	
	class Meta:
		model = Ejercicio
		exclude = ['usuario']

	tipo = forms.ChoiceField(choices = Ejercicio.TIPO,required=True, widget=forms.RadioSelect(attrs=dict({})))
	zona = forms.ChoiceField(choices = Ejercicio.ZONA,required=True, widget=forms.RadioSelect(attrs=dict({})))
	jurisdiccion = forms.ChoiceField(choices = Publicacion.JURISDICCION,required=True, widget=forms.Select(attrs=dict({})))
	categoria = forms.ChoiceField(choices = Publicacion.CATEGORIA,required=True, widget=forms.Select(attrs=dict({})))
	objetivo = forms.CharField(required=True, widget=forms.Textarea(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Objetivo','required':'required', 'style':'text-align:left'})))
	nombre = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Nombre','required':'required', 'style':'text-align: left;'})))
	intensidad = forms.CharField(required=True, widget=forms.Textarea(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Intensidad','required':'required', 'style':'text-align:left'})))
	detalle = forms.CharField(required=True, widget=forms.Textarea(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Detalle','required':'required', 'style':'text-align:left'})))
	url = forms.URLField(max_length=200, required=False, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Ingrese Url','style':'text-align: left;'})))
	imagen = forms.ImageField(required=False,widget=forms.FileInput(attrs=dict({'id':'uploadImage1', 'type':'file','name':'images[1]','onchange':'previewImage(1);'})))
	#fuente = forms.CharField(required=False, max_length=150, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Ingrese la Fuente','style':'text-align: left;'})))
	
	#class="form-control" id="uploadImage1" type="file" name="images[1]" onchange="previewImage(1);"
	#foto = forms.ForeignKey(Fotos, on_delete = 'CASCADE')
	#intro = forms.CharField(required=False,widget=forms.TextInput(attrs=dict({'class':'form-control input-lg','placeholder':'Introduccion', 'style':'text-align: left;'})))
