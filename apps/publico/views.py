from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import PublicacionForm

# Create your views here.

def home(request):

	repetir = [1,2,3,4]

	return render(request,"index.html",{'nombre':"Adrian", 'rango' :repetir})



"""def publicacion(request):

	if request.method == 'POST':
		form = PublicacionForm(request.POST)

		if form.is_valid():
			return HttpResponseRedirect('/thanks/')

	else:
		form = PublicacionForm()


	return render(request,"publicacion.html",{'form': form})	"""