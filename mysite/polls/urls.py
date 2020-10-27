#FOTOS DENTRO DO ALBUM
#INFORMA OS NOMES DE CADA FOTO
#DO ALBUM POLLS
from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote' ),
]

#Path  1-parametro = Nome da rota
#Path  2-parametro = Nome do Arquivo
#Path  3-parametro = nome da função