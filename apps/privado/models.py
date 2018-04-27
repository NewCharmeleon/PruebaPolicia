from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from .validators import *

# Create your models here.
class Publicacion(models.Model):
	TIPO = ((1 , 'articulo'), (2, 'video'),)

	tipo = models.IntegerField(default=1,choices = TIPO, validators=[tipo_validacion])

	#descripcion = models.CharField(max_length=100)
	titulo = models.CharField(max_length=100, validators=[texto_validacion])
	contenido = models.TextField(validators=[texto_validacion])
	url = models.URLField()#validators=[url_validacion])
	fuente = models.CharField(max_length=100, validators=[texto_validacion])
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha_modificacion = models.DateTimeField(auto_now=True)
	fecha_publicacion = models.DateTimeField(blank=True, null=True)	
	fecha_archivado = models.DateTimeField(blank=True, null=True)
	imagen = models.ImageField(upload_to='publicaciones',null=True,blank=True)
	intro = models.CharField(max_length=250, null=True, blank=True, default=None)
	is_publicado = models.BooleanField(default=False)
	is_archivado = models.BooleanField(default=False)
	is_para_portada = models.BooleanField(default=False)
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
