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
				#form.publicacion=save(commit=false)
				#image = Image.open(publicacion.imagen)
        		#ancho, alto = image.size
        		#ratio_height = (800*alto)/ancho
        		#size = ( 800, ratio_height)
        		#image = image.resize(size, Image.ANTIALIAS)
        		#image.save(publicacion.imagen)
				publicacion.Redimensionar()
				publicacion.save()
				messages.success(request, "Borrador creado con exito!!!")
				return HttpResponseRedirect(reverse('dashboard'))
				
			except Exception as e:
				print(e)
				error = "Ocurrio un problema al guardar los datos"
				#return render(request, 'new_publicacion.html',{'form':form,'error':error})
		else:
			messages.error(request, "Error. Revise los datos mal cargados.")
			#print(form.errors)
			#return render(request,'new_publicacion.html',{'form': form})
	else:
		form = PublicacionForm()
		form.initial['tipo'] ='1'
	return render(request,'new_publicacion.html',{'form': form})

@login_required
def show_publicacion(request,id):

	publicacion=get_object_or_404(Publicacion, id=id)
	messages.success(request, "Borradores obtenidos con exito!!!")
	return render(request,'show_publicacion.html',{'publicacion':publicacion})

@login_required
def show_archivados(request):	
	publicaciones = Publicacion.objects.filter(fecha_archivado__isnull=False,is_publicado=False).order_by('fecha_archivado')
	if not len(publicaciones):
		messages.warning(request, "No existen publicaciones archivadas")
	else:	
		messages.success(request, "Publicaciones archivadas obtenidas con exito!!!")
	return render(request,'show_archivados.html',{'publicaciones':publicaciones})

@login_required
def show_publicados(request):	
	publicaciones = Publicacion.objects.filter(fecha_publicacion__isnull=False,fecha_archivado__isnull=True).order_by('fecha_publicacion')
	if not len(publicaciones):
		messages.warning(request, "No existen publicaciones")
	else:	
		messages.success(request, "Publicaciones obtenidas con exito!!!")
	return render(request,'show_publicados.html',{'publicaciones':publicaciones})	

@login_required
def show_portada(request):	
	publicaciones = Publicacion.objects.filter(fecha_publicacion__isnull=False, is_para_portada=True).order_by('fecha_publicacion')
	if not len(publicaciones):
		messages.warning(request, "No existen publicaciones en portada")
	else:	
		messages.success(request, "Publicaciones en portada obtenidas con exito!!!")
	return render(request,'show_portada.html',{'publicaciones':publicaciones})			

@login_required	
@permission_required('privado.change_publicacion', raise_exception=False)
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
@permission_required('privado.delete_publicacion', raise_exception=False)
def confirm_delete_publicacion(request,id):

	publicacion=get_object_or_404(Publicacion, id=id)
	messages.success(request, "Publicacion a eliminar!!!")
	return render(request,'confirm_delete_publicacion.html',{'publicacion':publicacion})
		
@login_required
@permission_required('privado.delete_publicacion', raise_exception=False)
def delete_publicacion(request,id):

	publicacion=get_object_or_404(Publicacion, id=id)
	publicacion.delete()
	messages.success(request, "Publicacion eliminada con exito!!!")
	return HttpResponseRedirect(reverse('dashboard'))

@login_required
@permission_required('privado.change_publicacion', raise_exception=False)
def publicar_publicacion(request,id):

	publicacion=get_object_or_404(Publicacion, id=id)
	publicacion.Publicar()
	messages.success(request, "Publicacion publicada con exito!!!")
	return HttpResponseRedirect(reverse('dashboard'))

@login_required
@permission_required('privado.change_publicacion', raise_exception=False)
def enviar_publicacion(request,id):
	publicaciones=Publicacion.objects.filter(is_publicado=True, is_para_portada=True)
	cantidad = len(publicaciones)
	if cantidad>6:
		messages.warning(request, "Debe despublicar alguna publicacion de la portada!!!")
	else:
		publicacion=get_object_or_404(Publicacion, id=id)
		
		publicacion.Enviar()
		messages.success(request, "Publicacion publicada en portada con exito!!!")
	return HttpResponseRedirect(reverse('dashboard'))	

@login_required
@permission_required('privado.change_publicacion', raise_exception=True)
def despublicar_publicacion(request,id):

	publicacion=get_object_or_404(Publicacion, id=id)
	publicacion.Despublicar()
	messages.success(request, "Publicacion despublicada en portada con exito!!!")
	return HttpResponseRedirect(reverse('dashboard'))	

@login_required
@permission_required('privado.change_publicacion', raise_exception=True)
def archivar_publicacion(request,id):

	publicacion=get_object_or_404(Publicacion, id=id)
	publicacion.Archivar()
	messages.success(request, "Publicacion archivada con exito!!!")
	return HttpResponseRedirect(reverse('dashboard'))	

@login_required
def dashboard_autoridad(request):
	autoridades = Autoridad.objects.order_by('cargo')
	#.filter(usuario = request.user)
	return render(request,'dashboard_autoridad.html',{'usuario':request.user,'autoridades':autoridades})

@login_required
@permission_required('privado.add_autoridad', raise_exception=True)
def new_autoridad(request):

	if request.method == 'POST':

		form = AutoridadForm(request.POST,request.FILES)
		print(form.errors)
		if form.is_valid():
			autoridad = Autoridad() #instancio una nueva publicacion
			autoridad.nombre = form.cleaned_data['nombre']
			autoridad.segundo_nombre = form.cleaned_data['segundo_nombre']
			autoridad.apellido = form.cleaned_data['apellido']
			autoridad.jerarquia = form.cleaned_data['jerarquia']
			autoridad.cargo = form.cleaned_data['cargo']
			autoridad.dependencia = form.cleaned_data['dependencia']
			autoridad.direccion_laboral = form.cleaned_data['direccion_laboral']
			autoridad.telefono_laboral = form.cleaned_data['telefono_laboral']
			autoridad.telefono = form.cleaned_data['telefono']
			autoridad.email = form.cleaned_data['email']
			autoridad.trayectoria = form.cleaned_data['trayectoria']
			autoridad.imagen = form.cleaned_data['imagen']
			autoridad.usuario = request.user


			try:
				#form.publicacion=save(commit=false)
				#image = Image.open(publicacion.imagen)
        		#ancho, alto = image.size
        		#ratio_height = (800*alto)/ancho
        		#size = ( 800, ratio_height)
        		#image = image.resize(size, Image.ANTIALIAS)
        		#image.save(publicacion.imagen)
				autoridad.Redimensionar()
				autoridad.save()
				messages.success(request, "Autoridad creada con exito!!!")
				return HttpResponseRedirect(reverse('show_autoridades'))
				
			except Exception as e:
				print(e)
				error = "Ocurrio un problema al guardar los datos"
				#return render(request, 'new_publicacion.html',{'form':form,'error':error})
		else:
			messages.error(request, "Error. Revise los datos mal cargados.")
			#print(form.errors)
			#return render(request,'new_publicacion.html',{'form': form})
	else:
		form = AutoridadForm()
		#form.initial['tipo'] ='1'
	return render(request,'new_autoridad.html',{'form': form})

@login_required
def show_autoridades(request):

	autoridades = Autoridad.objects.order_by('cargo')
	if not len(autoridades):
		messages.warning(request, "No existen autoridades")
	else:	
		messages.success(request, "Autoridades obtenidas con exito!!!")
	return render(request,'show_autoridades.html',{'autoridades':autoridades})

@login_required
def show_autoridad(request,id):

	autoridad=get_object_or_404(Autoridad, id=id)
	messages.success(request, "Autoridad obtenida con exito!!!")
	return render(request,'show_autoridad.html',{'autoridad':autoridad})


@login_required	
@permission_required('privado.change_autoridad', raise_exception=False)
def edit_autoridad(request, id):

	autoridad=get_object_or_404(Autoridad, id=id)
	if request.method == 'POST':
		form = AutoridadForm(request.POST, instance=autoridad)
		if form.is_valid():
						
			try:
				form.save()
				messages.success(request, "Autoridad editada con exito!!!")
				return HttpResponseRedirect(reverse('show_autoridades'))
				
			except Exception as e:
				#print(e)
				error = "Ocurrio un problema al guardar los datos"
				return render(request, 'edit_autoridad.html',{'form':form,'error':error})
	else:
		form = AutoridadForm(instance=autoridad)

	return render(request,"edit_autoridad.html",{'form': form})	

@login_required
#@permission_required('privado.delete_autoridad', raise_exception=False)
def confirm_delete_autoridad(request,id):

	autoridad=get_object_or_404(Autoridad, id=id)
	messages.success(request, "Autoridad a eliminar!!!")
	return render(request,'confirm_delete_autoridad.html',{'autoridad':autoridad})

@login_required
@permission_required('privado.delete_autoridad', raise_exception=False)
def delete_autoridad(request,id):

	autoridad=get_object_or_404(Autoridad, id=id)
	autoridad.delete()
	messages.success(request, "Autoridad eliminada con exito!!!")
	return HttpResponseRedirect(reverse('dashboard'))	

@login_required
@permission_required('privado.change_autoridad', raise_exception=False)
def publicar_autoridad(request,id):

	autoridad=get_object_or_404(Autoridad, id=id)
	autoridad.Publicar()
	messages.success(request, "Autoridad publicada con exito!!!")
	return HttpResponseRedirect(reverse('show_autoridades'))	

@login_required
@permission_required('privado.change_autoridad', raise_exception=False)
def enviar_autoridad(request,id):
	autoridades=Autoridad.objects.filter(is_publicado=True, is_para_portada=True)
	cantidad = len(autoridades)
	if cantidad>7:
		messages.warning(request, "Debe despublicar alguna Autoridad de la portada!!!")
	else:
		autoridad=get_object_or_404(Autoridad, id=id)
		
		autoridad.Enviar()
		messages.success(request, "Autoridad publicada en portada con exito!!!")
	return HttpResponseRedirect(reverse('show_autoridades'))	

@login_required
@permission_required('privado.change_autoridad', raise_exception=True)
def despublicar_autoridad(request,id):

	autoridad=get_object_or_404(Autoridad, id=id)
	autoridad.Despublicar()
	messages.success(request, "Autoridad despublicada en portada con exito!!!")
	return HttpResponseRedirect(reverse('show_autoridades'))	

@login_required
@permission_required('privado.change_autoridad', raise_exception=True)
def archivar_autoridad(request,id):

	autoridad=get_object_or_404(Autoridad, id=id)
	autoridad.Archivar()
	messages.success(request, "Autoridad archivada con exito!!!")
	return HttpResponseRedirect(reverse('show_autoridades'))	
