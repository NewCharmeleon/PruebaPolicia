from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):

	repetir = [1,2,3,4]

	return render(request,"index.html",{'nombre':"Adrian", 'rango' :repetir})