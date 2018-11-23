from django.shortcuts import render
from django.http import HttpResponseRedirect
from apps.privado.models import Publicacion
from apps.privado.models import Autoridad
from apps.privado.models import Dependencia
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

# Create your views here.

def home(request):
	return render(request,'indexBackup.html')
#Nuevas rutas del Backup de Joomla

def sistemas(request):
	return render(request,'sistemas.html')

def plataformas(request):
	return render(request,'plataformas.html')

def descargas(request):
	return render(request,'descargas.html')

def dependencias(request):
	return render(request,'dependencias.html')

def correo(request):
	return render(request,'correo.html')	
	#noticia=get_object_or_404(Publicacion, id=id)
	'''
	noticias = Publicacion.objects.filter(is_para_portada=True, is_publicado=True, tipo=1).order_by('-fecha_creacion')[:10]
	videos = Publicacion.objects.filter(is_para_portada=True, tipo=2)
	autoridad = Autoridad.objects.filter(is_para_portada=True, cargo_id__in=[1,2])
	'''
	

	#return render(request,"indexBackup.html",{'nombre':"Adrian", 'noticias' :noticias, 'videos':videos, 'autoridades':autoridad })
'''
def noticias(request):

	noticias = Publicacion.objects.filter(is_publicado=True, tipo=1).order_by('-fecha_creacion')
	videos = Publicacion.objects.filter(is_para_portada=True, tipo=2)
	jurisdiccion = Publicacion.JURISDICCION
	
	return render(request,"noticias.html",{'noticias' :noticias, 'videos':videos,"jurisdicciones":jurisdiccion})	


def noticia(request, id):

	noticia=get_object_or_404(Publicacion, id=id)
				
	return render(request,'noticia.html',{'noticia':noticia})
	
def autoridades(request):
	autoridadJefe = Autoridad.objects.filter(is_para_portada=True, cargo_id__in=[1,2])
	autoridadPlana = Autoridad.objects.filter(is_para_portada=True, cargo_id__in=[4])
	return render(request,'autoridades.html', {'autoridadesJefe' :autoridadJefe, 'autoridadesPlana':autoridadPlana})

def dependencias(request, id):
	jurisdiccion = id
	#dependencias = Dependencia.objects.filter(is_para_portada=True)
	dependencia = Dependencia.objects.filter(is_publicado=True, jurisdiccion__in=[jurisdiccion]).order_by('nombre')
	print ("hay")
	print(len(dependencia))
	return render(request,'dependencias.html', {'dependencias':dependencia})

def dependencia(request, id):
	#dependencias = Dependencia.objects.filter(is_para_portada=True)
	dependencia=get_object_or_404(Dependencia, id=id)
	print ("hay")
	#print(len(dependencia))
	return render(request,'dependencia.html', {'dependencia':dependencia})	

def comunidad(request):
	videos = Publicacion.objects.filter(is_publicado=True, tipo=2, categoria=2)

	return render(request,'comunidad.html',{'videos':videos})

def historia(request):
	return render(request,'historia.html')

def escuelas(request):
	return render(request,'escuelas.html')	
	#return HttpResponseRedirect(reverse('home',{'noticia':noticia}))	
'''
'''
def publicacion(request):

	if request.method == 'POST':
		form = PublicacionForm(request.POST)

		if form.is_valid():
			return HttpResponseRedirect('/thanks/')

	else:
		form = PublicacionForm()


	return render(request,"publicacion.html",{'form': form})'''		