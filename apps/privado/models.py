from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from .validators import *
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.core.validators import RegexValidator
from tinymce import models as tinymce_models

# Create your models here.


class Publicacion(models.Model):
	TIPO = ((1 , 'Articulo'), (2, 'Video'),)
	JURISDICCION = ((0, 'Provincial'),(1, 'Jefatura de Policia'),(2 , 'Unidad Regional Comodoro Rivadavia'), (3, 'Unidad Regional Esquel'),(4, 'Unidad Regional Puerto Madryn'),(5, 'Unidad Regional Trelew'),)
	CATEGORIA = ((0 , 'Informativo'), (1, 'Institucional'), (2, 'Comunidad'),(3, 'Otro'),)

	tipo = models.IntegerField(choices = TIPO, validators=[tipo_validacion])
	jurisdiccion = models.IntegerField(choices = JURISDICCION, validators=[tipo_validacion])
	categoria = models.IntegerField(choices = CATEGORIA, validators=[tipo_validacion])
	
	titulo = models.CharField(max_length=100, validators=[texto_validacion])
	#contenido = models.TextField(validators=[texto_validacion])
	contenido = tinymce_models.HTMLField()
	
	url = models.URLField()#validators=[url_validacion])
	fuente = models.CharField(max_length=200, validators=[texto_validacion])
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha_modificacion = models.DateTimeField(auto_now=True)
	fecha_publicacion = models.DateTimeField(blank=True, null=True)	
	fecha_archivado = models.DateTimeField(blank=True, null=True)
	intro = models.CharField(max_length=350, null=True, blank=True)
	is_publicado = models.BooleanField(default=False)
	is_archivado = models.BooleanField(default=False)
	is_para_portada = models.BooleanField(default=False)
	usuario = models.ForeignKey(User, on_delete = 'CASCADE', default=User)

	#content = HTMLField()
	
	def Publicar(self):
		self.fecha_publicacion=timezone.now()
		self.is_publicado = True
		if self.is_archivado:
			self.is_archivado = False
		self.save()

	def Enviar(self):
		self.is_para_portada = True
		if self.is_archivado:
			self.is_archivado = False
		self.save()	

	def Despublicar(self):
		self.is_para_portada = False
		self.save()


	def Archivar(self):
		self.fecha_archivado=timezone.now()
		self.is_archivado = True
		if self.is_para_portada:
			self.is_para_portada = False
		if self.is_publicado:
			self.is_publicado = False
		self.save()	

	def Redimensionar(self):
	   	#self.imagen.resize((320, 240))
   		#self.save()	
   		#Opening the uploaded image
		im = Image.open(self.imagen)

		output = BytesIO()

		#Resize/modify the image
		im = im.resize( (500,400) )

		#after modifications, save it to the output
		im.save(output, format='JPEG', quality=320)
		output.seek(0)

		#change the imagefield value to be the newley modifed image value
		self.imagen = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.imagen.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
		self.save()
		#super(Modify,self).save()


class PublicacionFoto(models.Model):
	publicacion = models.ForeignKey(Publicacion, on_delete = models.PROTECT, null=True)
	imagen = models.ImageField(upload_to='publicaciones',null=True,blank=True, validators=[imagen_validacion])
	
	def __unicode__(self,):
		return str(self.image)
	
	def Redimensionar(self):
	   	#self.imagen.resize((320, 240))
   		#self.save()	
   		#Opening the uploaded image
		im = Image.open(self.imagen)

		output = BytesIO()

		#Resize/modify the image
		im = im.resize( (500,400) )

		#after modifications, save it to the output
		im.save(output, format='JPEG', quality=320)
		output.seek(0)

		#change the imagefield value to be the newley modifed image value
		self.imagen = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.imagen.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
		self.save()
		#super(Modify,self).save()
	#imagen_publicacion = models.ForeignKey(Publicacion, on_delete = 'CASCADE')
	


class Cargo(models.Model):

	descripcion = models.CharField(max_length=50)

	def __str__(self):
		return self.descripcion.upper()
	
class Jerarquia(models.Model):

	descripcion = models.CharField(max_length=50)

	def __str__(self):
		return self.descripcion.upper()

class Lugar(models.Model):

	descripcion = models.CharField(max_length=50)

	def __str__(self):
		return self.descripcion.upper()
		



class Autoridad(models.Model):

	#telefono_regex = RegexValidator(regex=r'^(?:(?:00)?549?)?0?(?:11|[2368]\d)(?:(?=\d{0,2}15)\d{2})??\d{8}$/D', message="El telefono debe tener formato: '+999999999'. Hasta 15 digitos es permitido.")
	
	#JERARQUIA = ((1 , 'Crio. General'), (2, 'Crio. Mayor'), (3, 'Crio. Inspector'), (4, 'Comisario'),(5, 'SubCrio.'),(6, 'Of. Principal'),(7, 'Of. Inspector.'),(8, 'Of. SubInsp.'),(9, 'Retirado'),(10, 'Retirado en servicio'),)
	#CARGO = ((1 , 'Jefe de Policia'), (2, 'SubJefe de Policia'), (3, 'Secretario General'), (4, 'Director'), (5, 'Jefe de Area'), (6, 'SubJefe de Area'), (7, 'Jefe'), (8, 'SubJefe'),)
	#DEPENDENCIA = ((1 , 'Jefatura de Policia'), (2, 'Secretaria General'), (3, 'Direccion Seguridad'), (4, 'Direccion Recursos Humanos'),(5, 'Direccion Recursos Materiales'),(6, 'Direccion Policia Judicial'),)

	jerarquia = models.ForeignKey(Jerarquia, on_delete = 'CASCADE')
	cargo = models.ForeignKey(Cargo, on_delete = 'CASCADE')
	lugar = models.ForeignKey(Lugar, on_delete = 'CASCADE')

	
	nombre = models.CharField(max_length=20, validators=[texto_validacion])
	segundo_nombre = models.CharField(max_length=20, validators=[texto_validacion])
	apellido = models.CharField(max_length=20, validators=[texto_validacion])
	imagen = models.ImageField(upload_to='autoridades',null=True,blank=True, validators=[imagen_validacion])
	direccion_laboral =  models.CharField(max_length=100, validators=[texto_validacion])
	telefono_laboral = models.CharField(validators=[telefono_validacion], max_length=35, blank=True)
	telefono = models.CharField(validators=[telefono_validacion], max_length=35, blank=True)
	email = models.EmailField()
	trayectoria = models.TextField(validators=[texto_validacion])
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha_modificacion = models.DateTimeField(auto_now=True)
	fecha_publicacion = models.DateTimeField(blank=True, null=True)	
	fecha_archivado = models.DateTimeField(blank=True, null=True)
	is_publicado = models.BooleanField(default=False)
	is_archivado = models.BooleanField(default=False)
	is_para_portada = models.BooleanField(default=False)
	
	#phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
	usuario = models.ForeignKey(User, on_delete = 'CASCADE', default=User)
	
	def nombre_completo(self):
		return '%s %s %s' % (self.nombre, self.segundo_nombre, self.apellido)

	def Convertir(self):
	

		im = Image.open(self.imagen).convert('RGBA')
		background = Image.new('RGBA', im.size, (255,255,255))

		alpha_composite = Image.alpha_composite(background, im)
		output = BytesIO() #prueba
		alpha_composite.save(output, 'JPEG', quality=80)

		output.seek(0)
		#change the imagefield value to be the newley modifed image value
		self.imagen = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.imagen.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
		self.save()
	

	def Publicar(self):
		self.fecha_publicacion=timezone.now()
		self.is_publicado = True
		if self.is_archivado:
			self.is_archivado = False
		self.save()

	def Enviar(self):
		self.is_para_portada = True
		if self.is_archivado:
			self.is_archivado = False
		self.save()	

	def Despublicar(self):
		self.is_para_portada = False
		self.save()


	def Archivar(self):
		self.fecha_archivado=timezone.now()
		self.is_archivado = True
		if self.is_para_portada:
			self.is_para_portada = False
		if self.is_publicado:
			self.is_publicado = False
		self.save()	

class Dependencia(models.Model):

	JURISDICCION = ((0, 'Provincial'),(1, 'Jefatura de Policia'),(2 , 'Unidad Regional Comodoro Rivadavia'), (3, 'Unidad Regional Esquel'),(4, 'Unidad Regional Puerto Madryn'),(5, 'Unidad Regional Trelew'),)
	FUNCION = ((0, 'Seguridad'),(1, 'Escuela'),)

	jurisdiccion = models.IntegerField(choices = JURISDICCION, validators=[tipo_validacion])
	funcion = models.IntegerField(choices = FUNCION, validators=[tipo_validacion])
	nombre = models.CharField(max_length=50, validators=[texto_validacion])
	direccion = models.CharField(max_length=100, validators=[texto_validacion])
	ciudad = models.CharField(max_length=100, validators=[texto_validacion])
	telefono = models.CharField(validators=[telefono_validacion], max_length=35, blank=True)
	email = models.EmailField()
	jefe = models.CharField(max_length=50, validators=[texto_validacion])
	subjefe = models.CharField(max_length=50, validators=[texto_validacion])
	ubicacion = models.CharField(max_length=150, validators=[ubicacion_validacion])
	imagen = models.ImageField(upload_to='dependencias',null=True,blank=True, validators=[imagen_validacion])
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha_modificacion = models.DateTimeField(auto_now=True)
	fecha_publicacion = models.DateTimeField(blank=True, null=True)	
	fecha_archivado = models.DateTimeField(blank=True, null=True)
	is_publicado = models.BooleanField(default=False)
	is_archivado = models.BooleanField(default=False)
	is_para_portada = models.BooleanField(default=False)
	
	#phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
	usuario = models.ForeignKey(User, on_delete = 'CASCADE', default=User)
	
	def Publicar(self):
		self.fecha_publicacion=timezone.now()
		self.is_publicado = True
		if self.is_archivado:
			self.is_archivado = False
		self.save()

	def Enviar(self):
		self.is_para_portada = True
		if self.is_archivado:
			self.is_archivado = False
		self.save()	

	def Despublicar(self):
		self.is_para_portada = False
		self.save()


	def Archivar(self):
		self.fecha_archivado=timezone.now()
		self.is_archivado = True
		if self.is_para_portada:
			self.is_para_portada = False
		if self.is_publicado:
			self.is_publicado = False
		self.save()	

	def Redimensionar(self):
	   	#self.imagen.resize((320, 240))
   		#self.save()	
   		#Opening the uploaded image
		im = Image.open(self.imagen)

		output = BytesIO()

		#Resize/modify the image
		im = im.resize( (500,400) )

		#after modifications, save it to the output
		im.save(output, format='JPEG', quality=320)
		output.seek(0)

		#change the imagefield value to be the newley modifed image value
		self.imagen = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.imagen.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)
		self.save()
		#super(Modify,self).save()	