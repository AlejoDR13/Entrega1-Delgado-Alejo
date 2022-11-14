from django.db import models

# Create your models here.

class Drama(models.Model):
    titulo = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    estreno = models.DateField()
    duracion = models.IntegerField()
    epigrafe = models.CharField(max_length=100)
    def __str__(self) -> str:
        return f"Titulo: {self.titulo}- direccion: {self.direccion} "

class Terror(models.Model):
    titulo = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    estreno = models.DateField()
    duracion = models.IntegerField()
    epigrafe = models.CharField(max_length=100)
    def __str__(self) -> str:
        return f"Titulo: {self.titulo}- direccion: {self.direccion} "

class Aventura(models.Model):
    titulo = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    estreno = models.DateField()
    duracion = models.IntegerField()
    epigrafe = models.CharField(max_length=100)
    def __str__(self) -> str:
        return f"Titulo: {self.titulo}- direccion: {self.direccion} "
class Ciencia_Ficcion(models.Model):
    titulo = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    estreno = models.DateField()
    duracion = models.IntegerField()
    epigrafe = models.CharField(max_length=100)
    def __str__(self) -> str:
        return f"Titulo: {self.titulo}- direccion: {self.direccion} "
class Thriller(models.Model):
    titulo = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    estreno = models.DateField()
    duracion = models.IntegerField()
    epigrafe = models.CharField(max_length=100)
    def __str__(self) -> str:
        return f"Titulo: {self.titulo}- direccion: {self.direccion} "
class Suspenso(models.Model):
    titulo = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    estreno = models.DateField()
    duracion = models.IntegerField()
    epigrafe = models.CharField(max_length=100)
    def __str__(self) -> str:
        return f"Titulo: {self.titulo}- direccion: {self.direccion} "


#Consulta Pablo
class Categorias(models.Model):
    genero = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=40)

class Peliculas(models.Model):
    titulo = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    estreno = models.DateField()
    duracion = models.IntegerField()
    epigrafe = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)

#Falta: Clase Posts, Clase AutorDelPost, Clase Categorias (Aca irian drama, terror, etc)

#Falta todavia para esto

class Registro(models.Model):
    usarname = models.CharField(max_length=40)
    mail = models.EmailField()
    password = models.IntegerField()

