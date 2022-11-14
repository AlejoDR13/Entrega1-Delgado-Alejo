from django.db import models

# Create your models here.

class Drama(models.Model):
    titulo = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    estreno = models.DateField()
    duracion = models.IntegerField()
    epigrafe = models.CharField(max_length=100)

class Terror(models.Model):
    titulo = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    estreno = models.DateField()
    duracion = models.IntegerField()
    epigrafe = models.CharField(max_length=100)

class Aventura(models.Model):
    titulo = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    estreno = models.DateField()
    duracion = models.IntegerField()
    epigrafe = models.CharField(max_length=100)

class Ciencia_Ficcion(models.Model):
    titulo = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    estreno = models.DateField()
    duracion = models.IntegerField()
    epigrafe = models.CharField(max_length=100)

class Thriller(models.Model):
    titulo = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    estreno = models.DateField()
    duracion = models.IntegerField()
    epigrafe = models.CharField(max_length=100)

class Suspenso(models.Model):
    titulo = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    estreno = models.DateField()
    duracion = models.IntegerField()
    epigrafe = models.CharField(max_length=100)

#Falta todavia para esto

class Registro(models.Model):
    usarname = models.CharField(max_length=40)
    mail = models.EmailField()
    password = models.IntegerField()

