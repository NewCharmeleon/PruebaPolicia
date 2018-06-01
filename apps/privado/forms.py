from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db import models
from apps.publico.models import *
from datetime import datetime
from .models import *


class LoginForm(forms.Form):
	user = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control','placeholder':'Usuario'})))
	password = forms.CharField(widget=forms.PasswordInput(attrs=dict({'class':'form-control','placeholder':'Contraseña'})))

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
	url = forms.URLField(max_length=150, required=False, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Ingrese Url','style':'text-align: left;'})))
	fuente = forms.CharField(required=False, max_length=150, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Ingrese la Fuente','style':'text-align: left;'})))
	imagen = forms.ImageField(required=False,widget=forms.FileInput(attrs=dict({'id':'imagen1','onchange':'revisarImagen(this,1);'})))
	intro = forms.CharField(required=False,widget=forms.TextInput(attrs=dict({'class':'form-control input-lg','placeholder':'Introduccion', 'style':'text-align: left;'})))

class AutoridadForm(ModelForm):

	class Meta:
		model = Autoridad
		exclude = ['usuario']
	
	#telefono_regex = RegexValidator(regex=r'^[(\d](?:(?:00)?549?)?0?(?:11|[2\d\d\d]\d\d\d)[)\d](?:(?=\d{0,2}15)\d{2})??([-\s]\d{7,9}).+$', message="El telefono debe tener formato: '+999999999'. Hasta 15 digitos es permitido.")

	jerarquia = forms.ChoiceField(choices = Autoridad.JERARQUIA,required=True, widget=forms.Select(attrs=dict({})))
	cargo = forms.ChoiceField(choices = Autoridad.CARGO,required=True, widget=forms.Select(attrs=dict({})))
	dependencia = forms.ChoiceField(choices = Autoridad.DEPENDENCIA,required=True, widget=forms.Select(attrs=dict({})))
	
	nombre = forms.CharField(required=True, max_length=20, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Nombre','required':'required', 'style':'text-align: left;'})))
	segundo_nombre = forms.CharField(required=False, max_length=20, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Segundo Nombre', 'style':'text-align: left;'})))
	apellido = forms.CharField(required=True, max_length=20, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Apellido','required':'required', 'style':'text-align: left;'})))
	imagen = forms.ImageField(required=True,widget=forms.FileInput(attrs=dict({'id':'imagen1','onchange':'revisarImagen(this,1);'})))
	direccion_laboral =  forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Direccion Laboral','required':'required', 'style':'text-align: left;'})))
	telefono_laboral = forms.CharField(required=True, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Telefono Laboral','required':'required', 'style':'text-align: left;'})))
	#telefono_laboral = forms.CharField(required=True, validators=[telefono_regex])
	telefono = forms.CharField(required=True, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Telefono','required':'required', 'style':'text-align: left;'})))
	email = forms.EmailField(max_length=150, required=True, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Ingrese Email','style':'text-align: left;'})))
	trayectoria = forms.CharField(required=True, widget=forms.Textarea(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Trayectoria','required':'required', 'style':'text-align:left'})))
	
	
	