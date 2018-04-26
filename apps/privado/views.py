from django.shortcuts import render
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.

def login(request):

	if not request.user.is_authenticated:
		if request.method=='GET':
			form = LoginForm()
			return render(request,'login.html',{'form':form})
		if request.method == 'POST':
			form = LoginForm(request.POST)
			if form.is_valid():
				usuario = form.cleaned_data['user']
				pas = form.cleaned_data['password']
				user = authenticate(username = usuario, password = pas)
				if user is not None:
					auth_login(request,user)
					messages.success(request, 'Bienvenido usuario')
					return HttpResponseRedirect(reverse('dashboard'))
				else:
					error = 'Verifique su usuario y contraseña'
					return render(request,'login.html',{'form':form,'error':error})
			
	return HttpResponseRedirect(reverse('dashboard'))

@login_required
def dashboard(request):
	publicaciones = Publicacion.objects.order_by('fecha_creacion')
	#.filter(usuario = request.user)
	return render(request,'dashboard.html',{'usuario':request.user,'publicaciones':publicaciones})

def logout(request):
	auth_logout(request)  # cierra sesion
	return redirect(reverse('home')) # redirecciona a home

@login_required
@permission_required('privado.add_publicacion', raise_exception=True)
def new_publicacion(request):

	if request.method == 'POST':

		form = PublicacionForm(request.POST,request.FILES)
		print(form.errors)
		if form.is_valid():
			publicacion = Publicacion() #instancio una nueva publicacion
			publicacion.tipo = form.cleaned_data['tipo']
			publicacion.titulo = form.cleaned_data['titulo']
			publicacion.contenido = form.cleaned_data['contenido']
			publicacion.url = form.cleaned_data['url']
			publicacion.fuente = form.cleaned_data['fuente']
			publicacion.intro = form.cleaned_data['intro']
			publicacion.imagen = form.cleaned_data['imagen']
			publicacion.usuario = request.user
			try:
				publicacion.save()
				messages.success(request, "Publicacion creada con exito!!!")
				return HttpResponseRedirect(reverse('dashboard'))
				
			except Exception as e:
				print(e)
				error = "Ocurrio un problema al guardar los datos"
				#return render(request, 'new_publicacion.html',{'form':form,'error':error})
		else:
			messages.error(request, "Error. Revise los datos mal cargados.")
			#return render(request,'new_publicacion.html',{'form': form})
	else:
		form = PublicacionForm()
		form.initial['tipo'] ='1'
	return render(request,'new_publicacion.html',{'form': form})

@login_required
def show_publicacion(request,id):

	publicacion=get_object_or_404(Publicacion, id=id)
	messages.success(request, "Publicacion obtenida con exito!!!")
	return render(request,'show_publicacion.html',{'publicacion':publicacion})

@login_required
def show_archivados(request):	
	publicaciones = Publicacion.objects.filter(fecha_archivado__isnull=False,is_publicado=False,usuario = request.user).order_by('fecha_archivado')
	if not len(publicaciones):
		messages.warning(request, "No existen publicaciones archivadas")
	else:	
		messages.success(request, "Publicaciones archivadas obtenidas con exito!!!")
	return render(request,'show_archivados.html',{'publicaciones':publicaciones})

@login_required
def show_publicados(request):	
	publicaciones = Publicacion.objects.filter(fecha_publicacion__isnull=False,fecha_archivado__isnull=True, usuario = request.user).order_by('fecha_publicacion')
	if not len(publicaciones):
		messages.warning(request, "No existen publicaciones")
	else:	
		messages.success(request, "Publicaciones publicadas obtenidas con exito!!!")
	return render(request,'show_publicados.html',{'publicaciones':publicaciones})	

@login_required
def show_portada(request):	
	publicaciones = Publicacion.objects.filter(fecha_publicacion__isnull=False, is_para_portada=True,usuario = request.user).order_by('fecha_publicacion')
	if not len(publicaciones):
		messages.warning(request, "No existen publicaciones en portada")
	else:	
		messages.success(request, "Publicaciones en portada obtenidas con exito!!!")
	return render(request,'show_portada.html',{'publicaciones':publicaciones})			

@login_required	
@permission_required('publicacion.change_publicacion', raise_exception=False)
def edit_publicacion(request, id):

	publicacion=get_object_or_404(Publicacion, id=id)
	if request.method == 'POST':
		form = PublicacionForm(request.POST, instance=publicacion)
		if form.is_valid():
						
			try:
				form.save()
				messages.success(request, "Publicacion editada con exito!!!")
				return HttpResponseRedirect(reverse('dashboard'))
				
			except Exception as e:
				#print(e)
				error = "Ocurrio un problema al guardar los datos"
				return render(request, 'edit_publicacion.html',{'form':form,'error':error})
	else:
		form = PublicacionForm(instance=publicacion)

	return render(request,"edit_publicacion.html",{'form': form})	

@login_required
@permission_required('publicacion.delete_publicacion', raise_exception=False)
def confirm_delete_publicacion(request,id):

	publicacion=get_object_or_404(Publicacion, id=id)
	messages.success(request, "Publicacion a eliminar!!!")
	return render(request,'confirm_delete_publicacion.html',{'publicacion':publicacion})
		
@login_required
def delete_publicacion(request,id):

	publicacion=get_object_or_404(Publicacion, id=id)
	publicacion.delete()
	messages.success(request, "Publicacion eliminada con exito!!!")
	return HttpResponseRedirect(reverse('dashboard'))

@login_required
@permission_required('publicacion.change_publicacion', raise_exception=False)
def publicar_publicacion(request,id):

	publicacion=get_object_or_404(Publicacion, id=id)
	publicacion.Publicar()
	messages.success(request, "Publicacion publicada con exito!!!")
	return HttpResponseRedirect(reverse('dashboard'))

@login_required
@permission_required('publicacion.change_publicacion', raise_exception=False)
def enviar_publicacion(request,id):
	publicaciones=Publicacion.objects.filter(is_publicado=True, is_para_portada=True)
	cantidad = len(publicaciones)
	if cantidad>5:
		messages.warning(request, "Debe despublicar alguna publicacion de la portada!!!")
	else:
		publicacion=get_object_or_404(Publicacion, id=id)
		
		publicacion.Enviar()
		messages.success(request, "Publicacion publicada en portada con exito!!!")
	return HttpResponseRedirect(reverse('dashboard'))	

@login_required
@permission_required('publicacion.change_publicacion', raise_exception=True)
def despublicar_publicacion(request,id):

	publicacion=get_object_or_404(Publicacion, id=id)
	publicacion.Despublicar()
	messages.success(request, "Publicacion despublicada en portada con exito!!!")
	return HttpResponseRedirect(reverse('dashboard'))	

@login_required
@permission_required('publicacion.change_publicacion', raise_exception=True)
def archivar_publicacion(request,id):

	publicacion=get_object_or_404(Publicacion, id=id)
	publicacion.Archivar()
	messages.success(request, "Publicacion archivada con exito!!!")
	return HttpResponseRedirect(reverse('dashboard'))	