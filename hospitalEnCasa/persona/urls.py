from django.urls import path
from . import views

urlpatterns = [
    path('auxiliar', views.consultarPaciente, name = 'Consulta'),
    path('nuevoPaciente', views.nuevoPaciente, name = 'registroPaciente'),
    path('nuevoDoctor', views.nuevoDoctor, name = 'registroDoctor'),
]
