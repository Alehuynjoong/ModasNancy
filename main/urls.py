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
        url(r'^Pide_Tu_Cita$', views.Pide_Tu_Cita, name="Pide_Tu_Cita"),         
        url(r'^Presentaciones$', views.Presentaciones, name="Presentaciones"),         
        url(r'^Primeras_Comuniones$', views.Primeras_Comuniones, name="Primeras_Comuniones"),         
        url(r'^XV_anios$', views.XV_anios, name="XV_anios"),     
        url(r'^registro$', views.registro, name="registro"),     
        url(r'^iniciodesesion$', views.iniciodesesion, name="iniciodesesion"),     
]    
#        url(r'^alta/productos$', views.creaProducto, name="creaProducto"), 
#        url(r'^editar/productos/(?P<pk>\d+)$', views.editarProducto, name="editarProducto") #?P es para agregarle un parametro,  <ahi va el parametro> y \d+ es la expresion regular de digito,  y el + es que espera minimo un digito
#        url(r'^productos$', views.Producto, name="productos"), 
