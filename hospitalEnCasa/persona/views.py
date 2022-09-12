from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
import json

from .models import Persona


# Create your views here.
def nuevaPersona(request):
    if request.method == 'GET':
        try:
            data = json.loads(request.body)
            persona = Persona(
                id = data ["id"],
                nombres = data["nombres"],
                apellidos = data["apellidos"],
                celular = data["celular"]
                )
            persona.save()
            return HttpResponse("Nueva persona agregada")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def consultarPacientes(request):
    if request.method == 'GET':
        personas = Persona.objects.all()
        if (not personas):
            return HttpResponseBadRequest("No existen personas en la bd")
        personasData = []
        for x in personas:
            #fechaStr =x.fechaNacimiento.strftime("%Y-%m-%d",)
            data = {"nombres": x.nombres, "apellidos":x.apellidos}
            personasData.append(data)
        dataJson = json.dumps(personasData)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def buscarPaciente(request, id):
    if request.method == 'GET':
        persona = Persona.objects.filter(id=id).first()
        if (not persona):
            return HttpResponseBadRequest("No existe la persona con esa cédula")
        data = {"id":persona.id, "nombres": persona.nombres, 
        "apellidos":persona.apellidos, "celular":persona.celular}
        dataJson = json.dumps(data)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

# def nuevoPaciente(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             persona = Persona(
#                 id = data ["id"],
#                 nombres = data["nombres"],
#                 apellidos = data["apellidos"],
#                 celular = data["celular"]
#                 )
#             paciente = Paciente(
#                 direccion = data["direccion"],
#                 ciudad = data["ciudad"],
#                 fechaNacimiento = data["fechaNacimiento"]
#                 )
#             persona.save()
#             paciente.save()
#             return HttpResponse("Nuevo paciente agregadoo")
#         except:
#             return HttpResponseBadRequest("Error en los datos enviados")
#     else:
#         return HttpResponseNotAllowed(['POST'], "Método inválido")

# def nuevoDoctor(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             persona = Persona(
#                 id = data ["id"],
#                 nombres = data["nombres"],
#                 apellidos = data["apellidos"],
#                 celular = data["celular"],
#                 )
#             persona.save()

#             doctor = Doctor(
#                 registro = data["registro"],
#                 especialidad = data["especialidad"],
#                 idDoctor = data["id"]
#                 )
            
#             doctor.save()
#             return HttpResponse("Nuevo doctor agregadoo")
#         except:
#             return HttpResponseBadRequest("Error en los datos enviados de doctor")
#     else:
#         return HttpResponseNotAllowed(['POST'], "Método inválido")


# def nuevoFamiliar(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            persona = Persona(
                id = data ["id"],
                nombres = data["nombres"],
                apellidos = data["apellidos"],
                celular = data["celular"],
                )
            familiar = Familiar(
                idFamiliar = data["id"],
                pacienteAsig = data["PacienteAsig"],
                parentesco = data["parentesco"],
                correo = ["correo"],
                )
            persona.save()
            familiar.save()
            return HttpResponse("Nuevo familiar agregadoo")
        except:
            return HttpResponseBadRequest("Error en los datos enviados de familiar")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

