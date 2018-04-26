from django.shortcuts import render
from django.http import HttpResponseRedirect
from apps.privado.models import Publicacion
#from .forms import PublicacionForm

# Create your views here.

def home(request):

	noticias = Publicacion.objects.filter(is_para_portada=True, tipo=1)
	videos = Publicacion.objects.filter(is_para_portada=True, tipo=2)

	return render(request,"index.html",{'nombre':"Adrian", 'noticias' :noticias, 'videos':videos})



"""def publicacion(request):

	if request.method == 'POST':
		form = PublicacionForm(request.POST)

		if form.is_valid():
			return HttpResponseRedirect('/thanks/')

	else:
		form = PublicacionForm()


	return render(request,"publicacion.html",{'form': form})	"""