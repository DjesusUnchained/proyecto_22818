from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.template import loader

# Create your views here.
def index(request):
    if(request.method=='GET'):
        titulo = 'Titulo cuando accedo por GET - MODIFICO EL VALOR'
    else:
        titulo = f'Titulo cuando accedo por otro metodo {request.method}'
    parametetros_get = request.GET.get('nombre')
    listado_cursos = [
        {
            'nombre':'Fullstack Java',
            'descripcion': 'Curso curso',
            'categoria':'Programación'
        },
        {
            'nombre':'Diseño UX/UI',
            'descripcion': '🎨',
            'categoria':'Diseño'
        },
        {
            'nombre':'Big Data',
            'descripcion': 'test test',
            'categoria':'Analisis de datos'
        },
    ]
    return render(request,'cac/index.html',{'titulo':titulo,'cursos':listado_cursos})
    # return HttpResponse(f"""
    #     <h1>{titulo}</h1>
    #     <p>{parametetros_get}</p>
    # """)


def quienes_somos(request):
    #return redirect('saludar_solito')
    #return redirect(reverse('saludar', kwargs={'nombre': 'PepaPig'}))
    template = loader.get_template('cac/quienes_somos.html')
    contexto = {'titulo':'Codo a Codo - Quienes Somos'}
    return HttpResponse(template.render(contexto,request))

def ver_proyectos(request,anio=2022,mes=1):
    proyectos = []
    return render(request,'cac/proyectos.html',{'proyectos':proyectos})

def ver_cursos(request,anio=2022,mes=1):
    listado_cursos = [
        {
            'nombre':'Fullstack Java',
            'descripcion': 'Curso curso',
            'categoria':'Programación'
        },
        {
            'nombre':'Diseño UX/UI',
            'descripcion': '🎨',
            'categoria':'Diseño'
        },
        {
            'nombre':'Big Data',
            'descripcion': 'test test',
            'categoria':'Analisis de datos'
        },
    ]
    return render(request,'cac/cursos.html',{'cursos':listado_cursos})
  
