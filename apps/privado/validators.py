from django.core.exceptions import ValidationError
from django.db import models

def tipo_validacion(valor):
	if type(valor)!=int: 
		raise ValidationError("No ha elegido un tipo correcto")

def texto_validacion(valor):
	if (valor == ''):
		raise ValidationError("No se permiten solo espacios en este campo")
	if (valor.isalnum() & valor.isspace()):
		raise ValidationError("Solo se permiten caracteres alfanumericos en este campo")
	if valor.isdigit():
		raise ValidationError("No se permiten solo numeros en el campo")	
	if valor.isupper():
		raise ValidationError("El campo no debe ser escrito todo en mayusculas") 
'''def url_validacion():
	if not URLField(value):
		raise ValidationError("El campo debe ser una URL valida")'''


			

	
	