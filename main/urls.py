from django.conf.urls import url
from django.contrib import admin
from .import views

#este es del main

urlpatterns=[
        url(r'^$',  views.home,  name="home"), 
        url(r'^index$', views.index, name="index"),  
        url(r'^Acerca_De$', views.Acerca_De, name="Acerca_De"),                
        url(r'^Catalogo$', views.Catalogo, name="Catalogo"),         
        url(r'^Contactanos$', views.Contactanos, name="Contactanos"),         
        url(r'^Novias$', views.Novias, name="Novias"),         
        url(r'^Pide_Tu_Cita$', views.creaCita, name="Pide_Tu_Cita"),
        url(r'^Presentaciones$', views.Presentaciones, name="Presentaciones"),         
        url(r'^Primeras_Comuniones$', views.Primeras_Comuniones, name="Primeras_Comuniones"),         
        url(r'^XV_anios$', views.XV_anios, name="XV_anios"),     
        url(r'^cita$', views.cita, name="cita"),     
        url(r'^usuarioRegistrado$', views.usuarioRegistrado, name="usuarioRegistrado"),     
        url(r'^registro$', views.creaUsuario, name="registro"),     
        url(r'^iniciodesesion$', views.iniciodesesion, name="iniciodesesion"),     
]  