from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Familiar(models.Model):

    nombre = models.CharField(max_length=40)
    numFavorito = models.IntegerField()
    comidaFavorita = models.CharField(max_length=20)
    fechaNac = models.DateField()