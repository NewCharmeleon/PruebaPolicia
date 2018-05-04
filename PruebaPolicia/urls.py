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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', public.home,name='home'),
    path('noticia/<id>/',public.noticia,name='noticia'),
    path('login/',private.login,name='login'),
    path('logout/',private.logout,name='logout'),
    path('dashboard/',private.dashboard,name='dashboard'),
    path('publicacion/new/',private.new_publicacion,name='new_publicacion'),
    path('publicacion/<int:id>/',private.show_publicacion,name='show_publicacion'),
    path('publicacion/<int:id>/edit/',private.edit_publicacion,name='edit_publicacion'),
    path('publicacion/<int:id>/confirm_delete/',private.confirm_delete_publicacion,name='confirm_delete_publicacion'),
    path('publicacion/<int:id>/delete/',private.delete_publicacion,name='delete_publicacion'),
    path('publicacion/<int:id>/publicar/',private.publicar_publicacion,name='publicar_publicacion'),
    path('publicacion/<int:id>/despublicar/',private.despublicar_publicacion,name='despublicar_publicacion'),
    path('publicacion/<int:id>/archivar/',private.archivar_publicacion,name='archivar_publicacion'),
    path('publicacion/<int:id>/portada/',private.enviar_publicacion,name='enviar_publicacion'),
    path('publicacion/publicados/',private.show_publicados,name='show_publicados'),
    path('publicacion/archivados/',private.show_archivados,name='show_archivados'),
    path('publicacion/portada/',private.show_portada,name='show_portada'),
    
    #path('publicacion/', public.publicacion,name='publicacion'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]