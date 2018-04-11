from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Publicacion(models.Model):
	TIPO = ((1 , 'articulo'), (2, 'video'),)

	tipo = models.IntegerField(choices = TIPO)
	descripcion = models.CharField(max_length=100)
	titulo = models.CharField(max_length=50)
	contenido = models.TextField()
	url = models.URLField()
	fuente = models.CharField(max_length=100)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	#fecha_creacion = models.DateTimeField(("Fecha de creacion"),default=datetime.now())
	usuario = models.ForeignKey(User, on_delete = 'CASCADE', default=User)