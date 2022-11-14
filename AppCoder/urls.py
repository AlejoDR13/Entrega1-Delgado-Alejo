from django.urls import path
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
    path('crear_drama/', views.crear_drama, name="AgregarDrama"),
    path('buscar_drama/', views.buscar_drama),

    #TERROR
    path('crear_terror/', views.crear_terror, name="AgregarTerror"),
    path('buscar_terror/', views.buscar_terror),

    #AVENTURA
    path('crear_aventura/', views.crear_aventura, name="AgregarAventura"),
    path('buscar_aventura/', views.buscar_aventura),

    #CIENCIA FICCION
    path('crear_cienciaficcion/', views.crear_cienciaficcion, name="AgregarCienciaFiccion"),
    path('buscar_cienciaficcion/', views.buscar_cienciaficcion),
    
    #THRILLER   
    path('crear_thriller/', views.crear_thriller, name="AgregarThriller"),
    path('buscar_thriller/', views.buscar_thriller),

    #SUSPENSO
    path('crear_suspenso/', views.crear_suspenso, name="AgregarSuspenso"),
    path('buscar_suspenso/', views.buscar_suspenso),
]