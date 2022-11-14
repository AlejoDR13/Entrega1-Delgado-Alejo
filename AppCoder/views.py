from django.http import HttpResponse
from django.shortcuts import render
from .forms import CrearDramaForm, CrearTerrorForm, CrearAventuraForm, CrearCienciaFiccionForm, CrearThrillerForm, CrearSuspensoForm
from .models import Drama, Terror, Aventura, Ciencia_Ficcion, Thriller, Suspenso

#INICIO
def padre(request):
    return render(request, 'AppCoder/templates/AppCoder/padre.html')

def sobremi(request):
    return render(request, 'AppCoder/templates/AppCoder/sobremi.html')

def sesion(request):
    return render(request, 'AppCoder/templates/AppCoder/sesion.html')

def registro(request):
    return render(request, 'AppCoder/templates/AppCoder/registro.html')

#DRAMA
def drama(request):
    return render(request, 'AppCoder/templates/AppCoder/drama.html')

def crear_drama(request):

    if request.method == 'POST':

        formulario = CrearDramaForm(request.POST)
        
        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data
    
            drama = Drama (titulo=formulario_limpio['titulo'], direccion=formulario_limpio['direccion'], estreno=formulario_limpio['estreno'], duracion=formulario_limpio['duracion'], epigrafe=formulario_limpio['epigrafe'])
    
            drama.save()

            return render(request, 'AppCoder/templates/AppCoder/drama.html')
    
    else:
        formulario = CrearDramaForm

    return render(request, 'AppCoder/templates/AppCoder/posts.html', {'formulario': formulario})

def buscar_drama(request):

    if request.GET["titulo"]:
        titulo = request.GET["titulo"]

        peliculas = Drama.objects.filter(titulo__icontains=titulo)

        return render(request, 'AppCoder/templates/AppCoder/showing.html', {"peliculas":peliculas, "titulo":titulo})
    else:
        respuesta = "No se encontro el titulo buscado"

    return HttpResponse(respuesta)

#TERROR
def terror(request):
    return render(request, 'AppCoder/templates/AppCoder/terror.html')

def crear_terror(request):

    if request.method == 'POST':

        formulario = CrearTerrorForm(request.POST)
        
        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data
    
            drama = Terror (titulo=formulario_limpio['titulo'], direccion=formulario_limpio['direccion'], estreno=formulario_limpio['estreno'], duracion=formulario_limpio['duracion'], epigrafe=formulario_limpio['epigrafe'])
    
            drama.save()

            return render(request, 'AppCoder/templates/AppCoder/terror.html')
    
    else:
        formulario = CrearTerrorForm

    return render(request, 'AppCoder/templates/AppCoder/posts.html', {'formulario': formulario})

def buscar_terror(request):

    if request.GET["titulo"]:
        titulo = request.GET["titulo"]

        peliculas = Terror.objects.filter(titulo__icontains=titulo)

        return render(request, 'AppCoder/templates/AppCoder/showing.html', {"peliculas":peliculas, "titulo":titulo})
    else:
        respuesta = "No se encontro el titulo buscado"

    return HttpResponse(respuesta)

#AVENTURA
def aventura(request):
    return render(request, 'AppCoder/templates/AppCoder/aventura.html')

def crear_aventura(request):

    if request.method == 'POST':

        formulario = CrearAventuraForm(request.POST)
        
        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data
    
            drama = Aventura (titulo=formulario_limpio['titulo'], direccion=formulario_limpio['direccion'], estreno=formulario_limpio['estreno'], duracion=formulario_limpio['duracion'], epigrafe=formulario_limpio['epigrafe'])
    
            drama.save()

            return render(request, 'AppCoder/templates/AppCoder/aventura.html')
    
    else:
        formulario = CrearAventuraForm

    return render(request, 'AppCoder/templates/AppCoder/posts.html', {'formulario': formulario})

def buscar_aventura(request):

    if request.GET["titulo"]:
        titulo = request.GET["titulo"]

        peliculas = Aventura.objects.filter(titulo__icontains=titulo)

        return render(request, 'AppCoder/templates/AppCoder/showing.html', {"peliculas":peliculas, "titulo":titulo})
    else:
        respuesta = "No se encontro el titulo buscado"

    return HttpResponse(respuesta)

#CIENCIA FICCION
def ciencia_ficcion(request):
    return render(request, 'AppCoder/templates/AppCoder/ciencia_ficcion.html')

def crear_cienciaficcion(request):

    if request.method == 'POST':

        formulario = CrearCienciaFiccionForm(request.POST)
        
        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data
    
            drama = Ciencia_Ficcion (titulo=formulario_limpio['titulo'], direccion=formulario_limpio['direccion'], estreno=formulario_limpio['estreno'], duracion=formulario_limpio['duracion'], epigrafe=formulario_limpio['epigrafe'])
    
            drama.save()

            return render(request, 'AppCoder/templates/AppCoder/ciencia_ficcion.html')
    
    else:
        formulario = CrearTerrorForm

    return render(request, 'AppCoder/templates/AppCoder/posts.html', {'formulario': formulario})

def buscar_cienciaficcion(request):

    if request.GET["titulo"]:
        titulo = request.GET["titulo"]

        peliculas = Ciencia_Ficcion.objects.filter(titulo__icontains=titulo)

        return render(request, 'AppCoder/templates/AppCoder/showing.html', {"peliculas":peliculas, "titulo":titulo})
    else:
        respuesta = "No se encontro el titulo buscado"

    return HttpResponse(respuesta)

#THRILLER
def thriller(request):
    return render(request, 'AppCoder/templates/AppCoder/thriller.html')

def crear_thriller(request):

    if request.method == 'POST':

        formulario = CrearThrillerForm(request.POST)
        
        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data
    
            drama = Thriller (titulo=formulario_limpio['titulo'], direccion=formulario_limpio['direccion'], estreno=formulario_limpio['estreno'], duracion=formulario_limpio['duracion'], epigrafe=formulario_limpio['epigrafe'])
    
            drama.save()

            return render(request, 'AppCoder/templates/AppCoder/thriller.html')
    
    else:
        formulario = CrearTerrorForm

    return render(request, 'AppCoder/templates/AppCoder/posts.html', {'formulario': formulario})

def buscar_thriller(request):

    if request.GET["titulo"]:
        titulo = request.GET["titulo"]

        peliculas = Thriller.objects.filter(titulo__icontains=titulo)

        return render(request, 'AppCoder/templates/AppCoder/showing.html', {"peliculas":peliculas, "titulo":titulo})
    else:
        respuesta = "No se encontro el titulo buscado"

    return HttpResponse(respuesta)

#SUSPENSO
def suspenso(request):
    return render(request, 'AppCoder/templates/AppCoder/suspenso.html')

def crear_suspenso(request):

    if request.method == 'POST':

        formulario = CrearSuspensoForm(request.POST)
        
        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data
    
            drama = Suspenso (titulo=formulario_limpio['titulo'], direccion=formulario_limpio['direccion'], estreno=formulario_limpio['estreno'], duracion=formulario_limpio['duracion'], epigrafe=formulario_limpio['epigrafe'])
    
            drama.save()

            return render(request, 'AppCoder/templates/AppCoder/suspenso.html')
    
    else:
        formulario = CrearSuspensoForm

    return render(request, 'AppCoder/templates/AppCoder/posts.html', {'formulario': formulario})

def buscar_suspenso(request):

    if request.GET["titulo"]:
        titulo = request.GET["titulo"]

        peliculas = Suspenso.objects.filter(titulo__icontains=titulo)

        return render(request, 'AppCoder/templates/AppCoder/showing.html', {"peliculas":peliculas, "titulo":titulo})
    else:
        respuesta = "No se encontro el titulo buscado"

    return HttpResponse(respuesta)