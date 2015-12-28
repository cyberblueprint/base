from django.db import models
from django.contrib.auth.models import User

from datetime import *

# Create your models here.
class Empresa(models.Model):
	nombre = models.CharField(max_length=300)
	datos_generales = models.TextField()

	def __str__(self):
		return self.nombre

class Licencia(models.Model):
	PRODUCTOS = (
		(1, 'Vzor Suite'),
		(2, 'Vzor Cloud'),
	)
	usuario = models.ForeignKey(User)
	#empresa = models.OneToOneField(Empresa, primary_key=True)
	empresa = models.ManyToManyField(Empresa)
	numero_de_monitores = models.IntegerField()
	numero_de_pasos = models.IntegerField()
	token = models.DateTimeField()
	inicio = models.DateTimeField(auto_now_add=True)
	fin = models.DateTimeField()
	habilitado = models.BooleanField()
	producto = models.IntegerField(choices=PRODUCTOS)
