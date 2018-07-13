from django.core.exceptions import ValidationError
from django.db import models
import re

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


def telefono_validacion(valor):
		#telefono = re.sub( '/\D+/', '', valor);
		#devolver si coincidió con el regex
		patron = re.compile('^[(\d](?:(?:00)?549?)?0?(?:11|[2\d\d\d]\d\d\d)[)\d](?:(?=\d{0,2}15)\d{2})??([-\s]\d{7,9}).+$')
		patron2 = re.compile('^[(\d](?:(?:00)?549?)?0?(?:11|[2\d\d\d]\d\d\d)[)\d](?:(?=\d{0,2}15)\d{2})??([-\s]\d{7,9})*$')
		
		#patron='^[\\(](?:(?:00){0,1}549{0,1}){0,1}0{0,1}(?:11|2\\d\\d\\d|02\\d\\d|[2\\d\\d\\d])[\\)](?:(?=\\d{0,2}15)\\d{2,2}){0,1}(\\s\\d{7,7}).{1,}$)^[(\d](?:(?:00)?549?)?0?(?:11|[2\d\d\d]\d\d\d)[)\d](?:(?=\d{0,2}15)\d{2})??([-\s]\d{7,9}).+$\D'
		#patron='^\+?\d{1,3}?[- .]?\(?(?:\d{2,3})\)?[- .]?\d\d\d[- .]?\d\d\d\d$'  
		#testString = valor # fill this in
		if not (re.match(patron,valor)):
			print("Fallo 1")
			if not (re.match(patron2,valor)):
				print("Fallo 2")
				raise ValidationError("Formato invalido, formato correcto: (02xx) xxxxxx (2-7 digitos)")
			else:
	 			print("Paso")		
	 	

#def telefono_validacion(valor):
		#telefono = re.sub( '/\D+/', '', valor);
		#devolver si coincidió con el regex
#		patron = re.compile('^[(\d](?:(?:00)?549?)?0?(?:11|[2\d\d\d]\d\d\d)[)\d](?:(?=\d{0,2}15)\d{2})??([-\s]\d{7,9}).+$')
		#patron='^[\\(](?:(?:00){0,1}549{0,1}){0,1}0{0,1}(?:11|2\\d\\d\\d|02\\d\\d|[2\\d\\d\\d])[\\)](?:(?=\\d{0,2}15)\\d{2,2}){0,1}(\\s\\d{7,7}).{1,}$)^[(\d](?:(?:00)?549?)?0?(?:11|[2\d\d\d]\d\d\d)[)\d](?:(?=\d{0,2}15)\d{2})??([-\s]\d{7,9}).+$\D'
		#patron='^\+?\d{1,3}?[- .]?\(?(?:\d{2,3})\)?[- .]?\d\d\d[- .]?\d\d\d\d$'  
		#testString = valor # fill this in
#		if not (re.match(patron,valor)):
		#if not (matchArray = regex.findall(testString))
#			raise ValidationError("Formato invalido, formato correcto: (02xx) xxxxxx (- xxxxxx)")
	 	

def ubicacion_validacion(valor):
		
		patronWeb = re.compile('^(https://)*(www.google|goo)')
		if not (re.match(patronWeb, valor)):
			raise ValidationError("No es una direccion web de GoogleMaps valida.")
		else:
			patronLatLon = re.compile('@(-?\d+\.\d+),(-?\d+\.\d+),(\d+\.?\d?)+z')
		
			if not (re.match(patronLatLong,valor)):
			#if not (matchArray = regex.findall(testString))
				raise ValidationError("Formato invalido de ubicación de GoogleMaps")
	 


# the matchArray variable contains the list of matches
    	#phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="El telefono debe tener formato: '+999999999'. Hasta 15 digitos es permitido.")
    	
   
			

	
	