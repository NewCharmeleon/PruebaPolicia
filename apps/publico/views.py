from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from apps.privado.models import Publicacion
from apps.privado.models import Autoridad
from apps.privado.models import Dependencia
from apps.publico.models import Documento
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

def correo(request):
	return render(request,'correo.html')	
	#noticia=get_object_or_404(Publicacion, id=id)

def sinic_sat(request):
	#form = FileUploadForm()
	#if request.method == 'POST':
		#form = FileUploadForm(request.POST,request.FILES)
		#if form.is_valid():
			#form.save()
			#return redirect('sinic_sat')
	archivos_lista= Documento.objects.filter(file_category__in=[0]).order_by('id')
	paginator = Paginator(archivos_lista, 5)

	page = request.GET.get('page')
	archivos = paginator.get_page(page)
	print ("hay")
	print(len(archivos))
	#return render(request,'home.html',{'form':form,'archivos':archivos})
	return render(request,'sinic_sat.html',{'archivos':archivos})
#Nuevas rutas del Backup de Joomla

def anexos_rrhh(request):
	#archivos = Documento.objects.filter(file_category__in=[1]).order_by('id')
	print ("hay")
	#print(len(archivos))
	return render(request,'anexos-rrhh.html')#,{'archivos':archivos})

def modus_operandis(request):
	#archivos = Documento.objects.filter(file_category__in=[2]).order_by('id')
	print ("hay")
	#print(len(archivos))
	return render(request,'modus_operandis.html')#,{'archivos':archivos})

def vivienda(request):
	#archivos = Documento.objects.filter(file_category__in=[3]).order_by('id')
	print ("hay")
	#print(len(archivos))
	return render(request,'5-vivienda.html')#,{'archivos':archivos})

def finanzas(request):
	#archivos = Documento.objects.filter(file_category__in=[4]).order_by('id')
	print ("hay")
	#print(len(archivos))
	return render(request,'6-finanzas.html')#,{'archivos':archivos})
#Nuevas rutas del Backup de Joomla



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