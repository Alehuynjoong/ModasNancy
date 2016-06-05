from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required

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


def iniciodesesion (request):
	return render_to_response('iniciodesesion.html',{
		
		},RequestContext(request))

	
VAR = [1,2,3,4]


def reporte(request):
    response = HTTPResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename=unruly.csv'
    writer = csv.writer(response)
    writer.writerow(['Year','VAR'])
    writer.writerow([year,num])

    return response