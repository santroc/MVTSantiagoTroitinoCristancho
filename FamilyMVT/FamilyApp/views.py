from django.http import HttpResponse
from django.shortcuts import render
from FamilyApp.models import Familiar
from django.template import loader

# Create your views here.

def agregarFamiliar(self, nombre, numFavorito, comidaFavorita, FechaNac):

    familiar = Familiar(nombre = nombre, numFavorito = int(numFavorito), comidaFavorita = comidaFavorita, fechaNac = FechaNac)
    familiar.save()

    return HttpResponse(f'{familiar.nombre} {numFavorito} creado con exito')

def mostrarFamilia(self):

    listaFamiliares = Familiar.objects.all()

    datos = {'familiares' : listaFamiliares}

    plantilla = loader.get_template('mostrarFamilia.html')

    documento = plantilla.render(datos)

    return HttpResponse(documento) #Comment