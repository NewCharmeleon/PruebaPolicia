from django.shortcuts import render
from django.http import HttpResponseRedirect
from apps.privado.models import Publicacion
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

# Create your views here.

def home(request):

	noticias = Publicacion.objects.filter(is_para_portada=True, tipo=1)
	videos = Publicacion.objects.filter(is_para_portada=True, tipo=2)
	
	return render(request,"index.html",{'nombre':"Adrian", 'noticias' :noticias, 'videos':videos})
def noticias(request):

	noticias = Publicacion.objects.filter(is_publicado=True, tipo=1)
	videos = Publicacion.objects.filter(is_para_portada=True, tipo=2)
	
	return render(request,"noticias.html",{'noticias' :noticias, 'videos':videos})	


def noticia(request, id):

	noticia=get_object_or_404(Publicacion, id=id)
				
	return render(request,'noticia.html',{'noticia':noticia})
	
def autoridades(request):
	return render(request,'autoridades.html')

def comunidad(request):
	return render(request,'comunidad.html')

def historia(request):
	return render(request,'historia.html')

def escuelas(request):
	return render(request,'escuelas.html')	
	#return HttpResponseRedirect(reverse('home',{'noticia':noticia}))	
"""def publicacion(request):

	if request.method == 'POST':
		form = PublicacionForm(request.POST)

		if form.is_valid():
			return HttpResponseRedirect('/thanks/')

	else:
		form = PublicacionForm()


	return render(request,"publicacion.html",{'form': form})	"""