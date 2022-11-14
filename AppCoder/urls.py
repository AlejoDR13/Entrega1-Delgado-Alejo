from django.urls import path
from AppCoder.views import padre, drama, terror, aventura, ciencia_ficcion, thriller, suspenso, sobremi, sesion, registro, crear_drama, buscar_drama, crear_terror, buscar_terror, crear_aventura, buscar_aventura, crear_cienciaficcion, buscar_cienciaficcion, crear_thriller, buscar_thriller, crear_suspenso, buscar_suspenso
from AppCoder import views

urlpatterns = [
    path('padre/', views.padre, name="Inicio"),
    path('drama/', views.drama, name="Drama"),
    path('terror/', views.terror, name="Terror"),
    path('aventura/', views.aventura, name="Aventura"),
    path('ciencia_ficcion/', views.ciencia_ficcion, name="Ciencia Ficcion"),
    path('thriller/', views.thriller, name="Thriller"),
    path('suspenso/', views.suspenso, name="Suspenso"),
    path('sobremi/', views.sobremi, name="Sobre mi"),
    path('sesion/', views.sesion, name="Sesion"),
    path('registro/', views.registro, name="Registro"),

    #DRAMA
    path('crear_drama/', crear_drama, name="AgregarDrama"),
    path('buscar_drama/', views.buscar_drama),

    #TERROR
    path('crear_terror/', crear_terror, name="AgregarTerror"),
    path('buscar_terror/', views.buscar_terror),

    #AVENTURA
    path('crear_aventura/', crear_aventura, name="AgregarAventura"),
    path('buscar_aventura/', views.buscar_aventura),

    #CIENCIA FICCION
    path('crear_cienciaficcion/', crear_cienciaficcion, name="AgregarCienciaFiccion"),
    path('buscar_cienciaficcion/', views.buscar_cienciaficcion),
    
    #THRILLER   
    path('crear_thriller/', crear_thriller, name="AgregarThriller"),
    path('buscar_thriller/', views.buscar_thriller),

    #SUSPENSO
    path('crear_suspenso/', crear_suspenso, name="AgregarSuspenso"),
    path('buscar_suspenso/', views.buscar_suspenso),
]