from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from apps.privado.models import Publicacion
from apps.privado.models import Autoridad
from apps.privado.models import Dependencia
from apps.publico.models import Documento
#from apps.publico.models import Ejercicio
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
#...
from django.template import RequestContext
from django.shortcuts import render_to_response
#...


# Create your views here.

def home(request):
	#messages.info(request, "Bienvenido, actualmente la Web App se encuentra en Mantenimiento y puede presentar fallos.")
	return render(request,'indexBackup.html')
	
#Nuevas rutas del Backup de Joomla

def sistemas(request):
	return render(request,'sistemas.html')

def plataformas(request):
	return render(request,'plataformas.html')

def sistema_voto_electronico(request):
	return render(request,'sistema_voto_electronico.html')

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
	messages.success(request, "Dependencia obtenida con exito!!!")
	print ("hay")
	#print(len(dependencia))
	return render(request,'dependencia.html', {'dependencia':dependencia})

def correo(request):
	return render(request,'correo.html')	
	#noticia=get_object_or_404(Publicacion, id=id)

def educacion_fisica_tips(request):
	return render(request,'educacion_fisica_tips.html')

def educacion_fisica_tips_covid19(request):
	return render(request,'educacion_fisica_tips_covid19.html')	

def educacion_fisica_tips_tren_superior(request):
	return render(request,'educacion_fisica_tips_tren_superior.html')	    



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
	#form = FileUploadForm()
	#if request.method == 'POST':
		#form = FileUploadForm(request.POST,request.FILES)
		#if form.is_valid():
			#form.save()
			#return redirect('sinic_sat')
	archivos_lista= Documento.objects.filter(file_category__in=[1]).order_by('id')
	paginator = Paginator(archivos_lista, 5)

	page = request.GET.get('page')
	archivos = paginator.get_page(page)
	print ("hay")
	print(len(archivos))
	#return render(request,'home.html',{'form':form,'archivos':archivos})
	return render(request,'anexos-rrhh.html',{'archivos':archivos})

def modus_operandis(request):
	#form = FileUploadForm()
	#if request.method == 'POST':
		#form = FileUploadForm(request.POST,request.FILES)
		#if form.is_valid():
			#form.save()
			#return redirect('sinic_sat')
	archivos_lista= Documento.objects.filter(file_category__in=[2]).order_by('id')
	paginator = Paginator(archivos_lista, 5)

	page = request.GET.get('page')
	archivos = paginator.get_page(page)
	print ("hay")
	print(len(archivos))
	#return render(request,'home.html',{'form':form,'archivos':archivos})
	return render(request,'modus_operandis.html',{'archivos':archivos})

def vivienda(request):
	#form = FileUploadForm()
	#if request.method == 'POST':
		#form = FileUploadForm(request.POST,request.FILES)
		#if form.is_valid():
			#form.save()
			#return redirect('sinic_sat')
	archivos_lista= Documento.objects.filter(file_category__in=[3]).order_by('id')
	paginator = Paginator(archivos_lista, 5)

	page = request.GET.get('page')
	archivos = paginator.get_page(page)
	print ("hay")
	print(len(archivos))
	#return render(request,'home.html',{'form':form,'archivos':archivos})
	return render(request,'vivienda.html',{'archivos':archivos})

def finanzas(request):
	#form = FileUploadForm()
	#if request.method == 'POST':
		#form = FileUploadForm(request.POST,request.FILES)
		#if form.is_valid():
			#form.save()
			#return redirect('sinic_sat')
	archivos_lista= Documento.objects.filter(file_category__in=[4]).order_by('id')
	paginator = Paginator(archivos_lista, 5)

	page = request.GET.get('page')
	archivos = paginator.get_page(page)
	print ("hay")
	print(len(archivos))
	#return render(request,'home.html',{'form':form,'archivos':archivos})
	return render(request,'finanzas.html',{'archivos':archivos})

def comunicaciones(request):
	#form = FileUploadForm()
	#if request.method == 'POST':
		#form = FileUploadForm(request.POST,request.FILES)
		#if form.is_valid():
			#form.save()
			#return redirect('sinic_sat')
	archivos_lista= Documento.objects.filter(file_category__in=[5]).order_by('id')
	paginator = Paginator(archivos_lista, 5)

	page = request.GET.get('page')
	archivos = paginator.get_page(page)
	print ("hay")
	print(len(archivos))
	#return render(request,'home.html',{'form':form,'archivos':archivos})
	return render(request,'comunicaciones.html',{'archivos':archivos})

def educacion_fisica(request):
	#form = FileUploadForm()
	#if request.method == 'POST':
		#form = FileUploadForm(request.POST,request.FILES)
		#if form.is_valid():
			#form.save()
			#return redirect('sinic_sat')
	archivos_lista= Documento.objects.filter(file_category__in=[6]).order_by('id')
	paginator = Paginator(archivos_lista, 5)

	page = request.GET.get('page')
	archivos = paginator.get_page(page)
	print ("hay")
	print(len(archivos))
	#return render(request,'home.html',{'form':form,'archivos':archivos})
	return render(request,'educacion_fisica.html',{'archivos':archivos})

#404: página no encontrada
def pag_404_not_found(request, exception, template_name='errors/404.html'):
	response = render_to_response('errors/404.html')
	response.status_code=404
	return response

#500: error en el servidor
def pag_500_error_server(request, exception,template_name='errors/500.html'):
	response = render_to_response('errors/500.html')
	response.status_code=500
	return response		

#Nuevas rutas del Backup de Joomla
	'''
	noticias = Publicacion.objects.filter(is_para_portada=True, is_publicado=True, tipo=1).order_by('-fecha_creacion')[:10]
	videos = Publicacion.objects.filter(is_para_portada=True, tipo=2)
	autoridad = Autoridad.objects.filter(is_para_portada=True, cargo_id__in=[1,2])
	'''
	

	#return render(request,"indexBackup.html",{'nombre':"Adrian", 'noticias' :noticias, 'videos':videos, 'autoridades':autoridad })

def noticias(request):

	noticias = Publicacion.objects.filter(is_publicado=True, tipo=1).order_by('-fecha_creacion')
	videos = Publicacion.objects.filter(is_para_portada=True, tipo=2)
	jurisdiccion = Publicacion.JURISDICCION
	
	return render(request,"noticias.html",{'noticias' :noticias, 'videos':videos,"jurisdicciones":jurisdiccion})

def noticia(request, id):

	noticia=get_object_or_404(Publicacion, id=id)
	return render(request,'noticia.html',{'noticia':noticia})
'''
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


	return render(request,"publicacion.html",{'form': form})
'''