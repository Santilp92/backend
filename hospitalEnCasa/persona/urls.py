from django.urls import path
from . import views

urlpatterns = [
    #urls de auxiliar
    path('auxiliar/nuevoPaciente', views.nuevaPersonaPaciente, name = 'RegistroPaciente'),
    path('auxiliar/consultarPacientes', views.consultarPersonasPacientes, name = 'ConsultarPacientes'),
    path('auxiliar/actualizarPaciente/<int:id>', views.actualizarPersonaPaciente, name = 'ActualizarPaciente'),
    path('auxiliar/borrarPaciente/<int:id>', views.borrarPersonaPaciente, name = 'EliminarPaciente'),
    path('auxiliar/buscarPersonaPaciente/<int:id>', views.buscarPersonaPaciente, name = 'BuscarPaciente'),


    #urls Persona
    path('nuevaPersona', views.nuevaPersona, name = 'RegistroPersona'),
    path('consultarPersonas', views.consultarPersonas, name = 'ConsultarTodos'), 
    path('buscarPersona/<int:id>', views.buscarPersona, name = 'ConsultarUno'), 
    path('actualizarPersona/<int:id>', views.actualizarPersona, name = 'Actualizar'),
    path('borrarPersona/<int:id>', views.borrarPersona, name = 'Eliminar'),

    #urls paciente
    path('actualizarPaciente/<int:id>', views.actualizarPaciente, name = 'actualizarPaciente'),
    path('nuevoPaciente', views.nuevoPaciente, name = 'RegistroPaciente'),
    path('borrarPaciente/<int:id>', views.borrarPaciente, name = 'EliminarPaciente'),
    # path('nuevoPaciente', views.nuevoPaciente, name = 'registroPaciente'),
    # path('nuevoDoctor', views.nuevoDoctor, name = 'registroDoctor'),
    
]
