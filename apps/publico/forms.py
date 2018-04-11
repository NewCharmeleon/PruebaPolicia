from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db import models
from apps.publico.models import *
from datetime import datetime




class PublicacionForm(ModelForm):
	class Meta:
		model = Publicacion
		exclude = []

	TIPO = ((1 , 'articulo'), (2, 'video'),)

	tipo = forms.ChoiceField(choices = TIPO,required=True, widget=forms.RadioSelect)

	descripcion = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Descripcion','style':'text-align: center;'})))
	titulo = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Titulo','required':'required', 'style':'text-align: center;'})))
	contenido = forms.CharField(required=True, widget=forms.Textarea(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Contenido','required':'required', 'style':'text-align:center'})))
	url = forms.URLField(max_length=100, required=True, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Ingrese Url','required':'required', 'style':'text-align: center;'})))
	fuente = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs=dict({'class':'form-control input-lg verifca','placeholder':'Ingrese la Fuente','style':'text-align: center;'})))
	
			


			

	
	