"""PruebaPolicia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from apps.publico import views as public
from apps.privado import views as private
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', public.home,name='home'),
    path('login/',private.login,name='login'),
    path('logout',private.logout,name='logout'),
    #path('publicacion/', private.publicacion,name='publicacion'),
    path('publicacion/', public.publicacion,name='publicacion'),
]
