#PONTO DE PARTIDA
#ALBUM DE FOTO POLLS
#retona ALGO NO NAVEGADOR
from django.http import HttpResponse

def index(request):
    return HttpResponse("Primeira Views!")

def testando (request):
    return HttpResponse("Uma Outra View!")