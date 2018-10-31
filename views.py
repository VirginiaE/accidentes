from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from accidentes.models import Accidente, Persona
from datetime import datetime

class AccidentesListView(ListView):
    model = Accidente

def accidente_detail(request, id_accidente):
    accidente = Accidente.objects.get(pk=id_accidente)
    personas = Accidente.objects.get(pk=id_accidente).personas.all()

    return render(request, 'accidentes/accidente_detail.html',{'accidente':accidente, 'personas':personas})

def registrar_accidente(request):
    temp_fecha_hora = datetime.strptime(request.GET['fecha'], '%d-%m-%YT%H:%M:%S')
    latitud = float(request.GET['latitud'])
    longitud = float(request.GET['longitud'])
    accidente = Accidente.objects.create(latitud=latitud, longitud=longitud, fecha_hora=temp_fecha_hora)

    for persona in request.GET['personas'].split('p'):
        sexo = 'Masculino' if persona.split(',')[0]=='M' else 'Femenino'
        persona = Persona.objects.create(sexo=sexo, sangre=persona.split(',')[1], edad=persona.split(',')[2])
        accidente.personas.add(persona)
    return HttpResponse("OK")