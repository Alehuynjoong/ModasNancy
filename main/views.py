from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.shortcuts import render, redirect
from .forms import CitasForm
from .forms import RegistroForm
from .forms import Catalogo


def index (request):
	return render_to_response('base.html',{
		
		},RequestContext(request))


def home (request):
	return render_to_response('home.html',{
		
		},RequestContext(request))


def Acerca_De (request):
	return render_to_response('Acerca_De.html',{
		
		},RequestContext(request))


def Catalogo (request):
	return render_to_response('Catalogo.html',{
		
		},RequestContext(request))


def Contactanos (request):
	return render_to_response('Contactanos.html',{
		
		},RequestContext(request))


def Novias (request):
	return render_to_response('Novias.html',{
		
		},RequestContext(request))


def Pide_Tu_Cita (request):
	return render_to_response('Pide_Tu_Cita.html',{
		
		},RequestContext(request))


def Presentaciones (request):
	return render_to_response('Presentaciones.html',{
		
		},RequestContext(request))


def Primeras_Comuniones (request):
	return render_to_response('Primeras_Comuniones.html',{
		
		},RequestContext(request))


def XV_anios (request):
	return render_to_response('XV_anios.html',{
		
		},RequestContext(request))


def registro (request):
	return render_to_response('registro.html',{
		
		},RequestContext(request))

def cita (request):
	return render_to_response('cita.html',{
		
		},RequestContext(request))


def usuarioRegistrado (request):
	return render_to_response('usuarioRegistrado.html',{
		
		},RequestContext(request))


def creaUsuario(request):
    formulario = RegistroForm()
    if request.method == 'POST':
        formulario = RegistroForm(request.POST, request.FILES,)
        if formulario.is_valid():
            formulario.save()
            return redirect('usuarioRegistrado')
    return render_to_response('registro.html', {
        'formularioRegistroUsuario': formulario,
        'titulo': 'Registro de usuario',
    }, RequestContext(request))


def creaRegistroCatalogo(request):
    formulario = RegistroCatalogoForm()
    if request.method == 'POST':
        formulario = RegistroCatalogoForm(request.POST, request.FILES,)
        if formulario.is_valid():
            formulario.save()
            return redirect('registroDeCatalogo')
    return render_to_response('XV_anios.html', {
        'formularioRegistroCatalogo': formulario,
        'titulo': 'Registro de item de Catalogo',
    }, RequestContext(request))


def creaCita(request):
    formulario = CitasForm()
    if request.method == 'POST':
        formulario = CitasForm(request.POST, request.FILES,)
        if formulario.is_valid():
            formulario.save()
            return redirect('cita')
    return render_to_response('Pide_Tu_Cita.html', {
        'formularioPideTuCita': formulario,
        'titulo': 'Alta de un producto',
    }, RequestContext(request))


def iniciodesesion (request):
	return render_to_response('iniciodesesion.html',{
		
		},RequestContext(request))