from django.shortcuts import render
from .forms import *
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse


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
					return HttpResponseRedirect(reverse('dashboard'))
				else:
					pass
			else:
				pass

	return HttpResponseRedirect(reverse('dashboard'))

def dashboard(request):
	publicaciones = Publicacion.objects.filter(usuario = request.user)
	return render(request,'dashboard.html',{'usuario':request.user,'publicaciones':publicaciones})

def logout(request):
	auth_logout(request)  # cierra sesion
	return redirect(reverse('home')) # redirecciona a home

def new_publicacion(request):

	if request.method == 'POST':
		form = PublicacionForm(request.POST)
		if form.is_valid():
			publicacion = Publicacion() #instancio una nueva publicacion
			publicacion.tipo = form.cleaned_data['tipo']
			publicacion.titulo = form.cleaned_data['titulo']
			publicacion.contenido = form.cleaned_data['contenido']
			publicacion.url = form.cleaned_data['url']
			publicacion.fuente = form.cleaned_data['fuente']
			publicacion.usuario = request.user
			try:
				publicacion.save()
				return render(request,'dashboard.html',{'usuario':request.user})
			except Exception as e:
				print(e)


	else:
		form = PublicacionForm()


	return render(request,'new_publicacion.html',{'form': form})

def show_publicacion(request,id):

	publicacion=get_object_or_404(Publicacion, id=id)
	return render(request,'show_publicacion.html',{'publicacion':publicacion})
		
	
def edit_publicacion(request, id):

	publicacion=get_object_or_404(Publicacion, id=id)
	if request.method == 'POST':
		form = PublicacionForm(request.POST, instance=publicacion)
		if form.is_valid():
			
			publicacion.tipo = form.cleaned_data['tipo']
			publicacion.titulo = form.cleaned_data['titulo']
			publicacion.contenido = form.cleaned_data['contenido']
			publicacion.url = form.cleaned_data['url']
			publicacion.fuente = form.cleaned_data['fuente']
			publicacion.usuario = request.user
			try:
				publicacion.save()
				return HttpResponseRedirect(reverse('dashboard'))
				#return redirect(request,'dashboard.html',{'usuario':request.user})
				#return redirect('dashboard.html',id=publicacion.id)
			except Exception as e:
				print(e)
	else:
		form = PublicacionForm(instance=publicacion)

	return render(request,"edit_publicacion.html",{'form': form})			