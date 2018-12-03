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
from django.conf.urls import include

urlpatterns = [
    #path('tinymce/', include('tinymce.urls')),
    #path('admin/', admin.site.urls),
    path('', public.home,name='home'),

    path('sistemas/', public.sistemas, name='sistemas'),
    path('plataformas/', public.plataformas, name='plataformas'),
    path('descargas/', public.descargas, name='descargas'),
    path('dependencias/<int:id>/', public.dependencias, name='dependencias'),
    path('dependencia/<int:id>/', public.dependencia, name='dependencia'),
    path('correo/', public.correo, name='correo'),
    
    #path('autoridades/', public.autoridades, name='autoridades'),
    #path('comunidad/', public.comunidad, name='comunidad'),
    #path('historia/', public.historia, name='historia'),
    #path('escuelas/', public.escuelas, name='escuelas'),
    #path('dependencias/<int:id>/', public.dependencias, name='dependencias'),
    #path('dependencia/<int:id>/', public.dependencia, name='dependencia'),
    #path('noticias/', public.noticias, name='noticias'),
    #path('noticia/<int:id>/',public.noticia,name='noticia'),
    #path('login/',private.login,name='login'),
    #path('logout/',private.logout,name='logout'),
    #path('dashboard/',private.dashboard,name='dashboard'),
    
    #path('autoridades/ver/',private.show_autoridades,name='show_autoridades'),
    #path('autoridad/new/',private.new_autoridad,name='new_autoridad'),
    #path('autoridad/<int:id>/',private.show_autoridad,name='show_autoridad'),
    #path('autoridad/<int:id>/edit/',private.edit_autoridad,name='edit_autoridad'),
    #path('autoridad/<int:id>/confirm_delete/',private.confirm_delete_autoridad,name='confirm_delete_autoridad'),
    #path('autoridad/<int:id>/delete/',private.delete_autoridad,name='delete_autoridad'),
    #path('autoridad/<int:id>/publicar/',private.publicar_autoridad,name='publicar_autoridad'),
    #path('autoridad/<int:id>/despublicar/',private.despublicar_autoridad,name='despublicar_autoridad'),
    #path('autoridad/<int:id>/archivar/',private.archivar_autoridad,name='archivar_autoridad'),
    #path('autoridad/<int:id>/portada/',private.enviar_autoridad,name='enviar_autoridad'),
    #path('autoridades/publicados/',private.show_autoridades_publicados,name='show_autoridades_publicados'),
    #path('autoridades/no-publicados/',private.show_autoridades_nopublicados,name='show_autoridades_nopublicados'),
    #path('autoridades/archivados/',private.show_autoridades_archivados,name='show_autoridades_archivados'),
    #path('autoridades/portada/',private.show_autoridades_portada,name='show_autoridades_portada'),

    #path('dependencias/ver/',private.show_dependencias,name='show_dependencias_ver'),
    #path('dependencia/new/',private.new_dependencia,name='new_dependencia'),
    #path('dependencias/<int:id>/ver/',private.show_dependencia,name='show_dependencia_ver'),
    #path('dependencia/<int:id>/edit/',private.edit_dependencia,name='edit_dependencia'),
    #path('dependencia/<int:id>/confirm_delete/',private.confirm_delete_dependencia,name='confirm_delete_dependencia'),   
    #path('dependencia/<int:id>/delete/',private.delete_dependencia,name='delete_dependencia'),
    #path('dependencia/<int:id>/publicar/',private.publicar_dependencia,name='publicar_dependencia'),
    #path('dependencia/<int:id>/despublicar/',private.despublicar_dependencia,name='despublicar_dependencia'),
    #path('dependencia/<int:id>/archivar/',private.archivar_dependencia,name='archivar_dependencia'),
    #path('dependencia/<int:id>/portada/',private.enviar_dependencia,name='enviar_dependencia'),
    #path('dependencias/publicados/',private.show_dependencias_publicados,name='show_dependencias_publicados'),
    #path('dependencias/no-publicados/',private.show_dependencias_nopublicados,name='show_dependencias_nopublicados'),
    #path('dependencias/archivados/',private.show_dependencias_archivados,name='show_dependencias_archivados'),
    #path('dependencias/portada/',private.show_dependencias_portada,name='show_dependencias_portada'),


    #path('publicacion/new/',private.new_publicacion,name='new_publicacion'),
    #path('publicacion/<int:id>/',private.show_publicacion,name='show_publicacion'),
    #path('publicacion/<int:id>/ver/',private.ver_publicacion,name='ver_publicacion'),
    #path('publicacion/<int:id>/edit/',private.edit_publicacion,name='edit_publicacion'),
    #path('publicacion/<int:id>/confirm_delete/',private.confirm_delete_publicacion,name='confirm_delete_publicacion'),
    #path('publicacion/<int:id>/delete/',private.delete_publicacion,name='delete_publicacion'),
    #path('publicacion/<int:id>/publicar/',private.publicar_publicacion,name='publicar_publicacion'),
    #path('publicacion/<int:id>/despublicar/',private.despublicar_publicacion,name='despublicar_publicacion'),
    #path('publicacion/<int:id>/archivar/',private.archivar_publicacion,name='archivar_publicacion'),
    #path('publicacion/<int:id>/portada/',private.enviar_publicacion,name='enviar_publicacion'),
    #path('publicacion/publicados/',private.show_publicados,name='show_publicados'),
    #path('publicacion/archivados/',private.show_archivados,name='show_archivados'),
    #path('publicacion/portada/',private.show_portada,name='show_portada'),
    
    #path('publicacion/', public.publicacion,name='publicacion'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]