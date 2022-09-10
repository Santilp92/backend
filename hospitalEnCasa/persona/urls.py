from django.urls import path
from . import views

urlpatterns = [
    path('auxiliar', views.consultarPaciente, name = 'Consulta'),
]
