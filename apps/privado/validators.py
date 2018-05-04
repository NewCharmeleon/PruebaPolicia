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

def imagen_validacion(valor):
        filesize = valor.file.size
        megabyte_limit = 5.0
        if filesize > megabyte_limit*1024*1024:
            raise ValidationError("El tamaño maximo del archivo debe ser de %sMB" % str(megabyte_limit))

			

	
	