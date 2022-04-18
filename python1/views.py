from datetime import datetime
from faulthandler import disable
from multiprocessing import context
from pipes import Template
from django.http import HttpResponse
from django.template import Template, Context
import datetime



def saludo(request):
    return HttpResponse("Hola tato soy la Aye, porfavor vení a mardel YA")

def segunda_vista(request):
    return HttpResponse("Este sale")

def diaHoy(request):
    dia = datetime.datetime.now()

    texto= f"Hoy dia es {dia}"

    return HttpResponse(texto)

def miNombre(request, nombre):
    texto = f"Mi nombre es {nombre}"
    return HttpResponse(texto)
    
def edad(request, edad):
    edad2 = int(edad)
    anio= datetime.datetime.today().year
    anio2= int(anio)
    nacimiento= anio2-edad2
    texto= f"Usted nació en el año {nacimiento}"
    return HttpResponse(texto)

def probandoTemplate(request):
    miHtlm = open("C:/Users/GABRIEL GAGGIOTTI/Desktop/python1/Plantillas/pagina1.html")
    plantilla = Template(miHtlm.read())
    miHtlm.close()
    miContexto= Context()
    documento= plantilla.render(miContexto)
    return HttpResponse(documento)
