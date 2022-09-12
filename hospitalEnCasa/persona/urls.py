from django.urls import path
from . import views

urlpatterns = [
    path('nuevaPersona', views.nuevaPersona, name = 'registroPersona'),
    path('consultarPacientes', views.consultarPacientes, name = 'ConsultarTodos'), 
    path('buscarPaciente/<int:id>', views.buscarPaciente, name = 'ConsultarUno'), 

    # path('nuevoPaciente', views.nuevoPaciente, name = 'registroPaciente'),
    # path('nuevoDoctor', views.nuevoDoctor, name = 'registroDoctor'),
    
]
