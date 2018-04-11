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
		exclude = ['usuario']

	TIPO = ((1 , 'articulo'), (2, 'video'),)

	tipo = forms.ChoiceField(choices = TIPO,required=True, widget=forms.RadioSelect)

	#descripcion = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Descripcion','style':'text-align: left;'})))
	titulo = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Titulo','required':'required', 'style':'text-align: left;'})))
	contenido = forms.CharField(required=True, widget=forms.Textarea(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Contenido','required':'required', 'style':'text-align:left'})))
	url = forms.URLField(max_length=100, required=False, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Ingrese Url','style':'text-align: left;'})))
	fuente = forms.CharField(required=False, max_length=100, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Ingrese la Fuente','style':'text-align: left;'})))
	
