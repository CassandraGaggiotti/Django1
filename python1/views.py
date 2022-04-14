from datetime import datetime
from faulthandler import disable
from django.http import HttpResponse
import datetime


def saludo(request):
    return HttpResponse("Hola tato soy la Aye, porfavor vení a mardel YA")

def segunda_vista(request):
    return HttpResponse("Este sale")

def diaHoy(request):
    dia = datetime.datetime.now()

    texto= f"Hoy dia es {dia}"

    return HttpResponse(texto)