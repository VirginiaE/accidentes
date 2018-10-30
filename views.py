from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from accidentes.models import Accidente,Persona

class AccidentesListView(ListView):
    model = Accidente

def accidente_detail(request, id_accidente):
    accidente = Accidente.objects.get(pk=id_accidente)
    personas = Accidente.objects.get(pk=id_accidente).personas.all()
    posicion = {'lat':accidente.latitud, 'long':accidente.longitud}

    return render(request, 'accidentes/accidente_detail.html',{'accidente':accidente, 'personas':personas, 'posicion':posicion})