from django import forms

class CrearDramaForm(forms.Form):
    titulo = forms.CharField(max_length=40)
    direccion = forms.CharField(max_length=40)
    estreno = forms.DateField()
    duracion = forms.IntegerField()
    epigrafe = forms.CharField(max_length=100)

class CrearTerrorForm(forms.Form):
    titulo = forms.CharField(max_length=40)
    direccion = forms.CharField(max_length=40)
    estreno = forms.DateField()
    duracion = forms.IntegerField()
    epigrafe = forms.CharField(max_length=100)

class CrearAventuraForm(forms.Form):
    titulo = forms.CharField(max_length=40)
    direccion = forms.CharField(max_length=40)
    estreno = forms.DateField()
    duracion = forms.IntegerField()
    epigrafe = forms.CharField(max_length=100)

class CrearCienciaFiccionForm(forms.Form):
    titulo = forms.CharField(max_length=40)
    direccion = forms.CharField(max_length=40)
    estreno = forms.DateField()
    duracion = forms.IntegerField()
    epigrafe = forms.CharField(max_length=100)

class CrearThrillerForm(forms.Form):
    titulo = forms.CharField(max_length=40)
    direccion = forms.CharField(max_length=40)
    estreno = forms.DateField()
    duracion = forms.IntegerField()
    epigrafe = forms.CharField(max_length=100)

class CrearSuspensoForm(forms.Form):
    titulo = forms.CharField(max_length=40)
    direccion = forms.CharField(max_length=40)
    estreno = forms.DateField()
    duracion = forms.IntegerField()
    epigrafe = forms.CharField(max_length=100)