from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from apps.privado.validators import *
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.core.validators import RegexValidator
from tinymce import models as tinymce_models


# Create your models here.

class Documento(models.Model):
	CATEGORIA = ((0 , 'SINIC-SAT'), (1, 'Anexo RRHH '),
	(2, 'ModusOperandis '),(3, 'Vivienda '), (4, 'Área Finanzas '),(5, 'Área Comunicaciones e Informatica '),(6, 'Departamento de Educacion Fisica '),)
	
	file_category = models.IntegerField(choices = CATEGORIA, validators=[tipo_validacion])
	file_logo = models.CharField(max_length=100, validators=[texto_validacion])
	file_name = models.CharField(max_length=100, validators=[texto_validacion])
	file_description    = models.CharField(max_length = 250)
	file_upload         = models.FileField(upload_to='documentos/')

	def nombre_documento(self):
		return '%s %s %s' % (self.file_category, self.file_name, self.file_description)


	class Meta:
		db_table = 'publico_documentos'


class Publicacion(models.Model):
	TIPO = ((1 , 'Articulo'), (2, 'Video'),)
	JURISDICCION = ((0, 'Provincial'),(1, 'Jefatura de Policia - Rawson'),(2 , 'Unidad Regional Comodoro Rivadavia'), (3, 'Unidad Regional Esquel'),(4, 'Unidad Regional Puerto Madryn'),(5, 'Unidad Regional Trelew'),)
	CATEGORIA = ((0 , 'Informativo'), (1, 'Institucional'), (2, 'Comunidad'),(3, 'Otro'),)

	tipo = models.IntegerField(choices = TIPO, validators=[tipo_validacion])
	jurisdiccion = models.IntegerField(choices = JURISDICCION, validators=[tipo_validacion])
	categoria = models.IntegerField(choices = CATEGORIA, validators=[tipo_validacion])
	
	titulo = models.CharField(max_length=100, validators=[texto_validacion])
	contenido = models.TextField(validators=[texto_validacion])
	#contenido = tinymce_models.HTMLField()
	imagen = models.ImageField(upload_to='publicaciones',null=True,blank=True, validators=[imagen_validacion])
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
	usuario = models.ForeignKey(User, related_name='users',on_delete = 'CASCADE')

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







	




	