#FOTOS DENTRO DO ALBUM
#INFORMA OS NOMES DE CADA FOTO
#DO ALBUM POLLS
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jonas', views.testando,name='testando'),
]

#Path  1-parametro = Nome da rota
#Path  2-parametro = Nome do Arquivo
#Path  3-parametro = nome da função