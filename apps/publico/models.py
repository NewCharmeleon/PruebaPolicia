from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Publicacion(models.Model):
	TIPO = ((1 , 'articulo'), (2, 'video'),)

	tipo = models.IntegerField(choices = TIPO)
	descripcion = models.CharField(max_length=100)
	titulo = models.CharField(max_length=50)
	contenido = models.TextField()
	url = models.URLField()
	fecha_creacion = models.DateField()
	fuente = models.CharField(max_length=100)
	usuario = models.ForeignKey(User, on_delete = 'CASCADE')