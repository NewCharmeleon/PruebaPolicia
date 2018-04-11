from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db import models
from apps.publico.models import *
from datetime import datetime


class LoginForm(forms.Form):
	user = forms.CharField(widget=forms.TextInput(attrs=dict({'class':'form-control','placeholder':'Usuario'})))
	password = forms.CharField(widget=forms.PasswordInput(attrs=dict({'class':'form-control','placeholder':'Contraseña'})))

class PublicacionForm(ModelForm):
	class Meta:
		model = Publicacion
		exclude = []

	TIPO = ((1 , 'articulo'), (2, 'video'),)

	tipo = forms.ChoiceField(choices = TIPO)

	descripcion = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Descripcion','style':'text-align: center;'})))
	titulo = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Titulo','required':'required', 'style':'text-align: center;'})))
	contenido = forms.CharField(required=True, widget=forms.Textarea(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Contenido','required':'required', 'style':'text-align:center'})))
	url = forms.URLField(required=True)
	fecha_creacion = datetime.now()
	fuente = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Fuente','style':'text-align: center;'})))
	
