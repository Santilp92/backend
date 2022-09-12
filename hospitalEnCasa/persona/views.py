from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
import json

from .models import Doctor, Paciente, Persona, Familiar


# Create your views here.

def consultarPaciente(request):
    return HttpResponse("Consultar paciente")

def nuevoPaciente(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            persona = Persona(
                id = data ["id"],
                nombres = data["nombres"],
                apellidos = data["apellidos"],
                celular = data["celular"]
                )
            paciente = Paciente(
                persona_ptr_id = data["id"], 
                direccion = data["direccion"],
                ciudad = data["ciudad"],
                fechaNacimiento = data["fechaNacimiento"]
                )
            paciente.save()
            persona.save()
            return HttpResponse("Nuevo paciente agregadoo")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def nuevoDoctor(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            persona = Persona(
                id = data ["id"],
                nombres = data["nombres"],
                apellidos = data["apellidos"],
                celular = data["celular"],
                )
            doctor = Doctor(
                registro = data["registro"],
                especialidad = data["especialidad"],
                )
            doctor.save()
            persona.save()
            return HttpResponse("Nuevo doctor agregadoo")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

# def getMember(request):
#     if request.method == 'GET':
#         members = Members.objects.all()
#         allMemberData = []
#         for x in members:
#             data = {"id": x.id, "name": x.name, "email":x.email}
#             allMemberData.append(data)
#         dataJson = json.dumps(allMemberData)
#         #print(dataJson)
#         resp = HttpResponse()
#         resp.headers['Content-Type'] = "text/json"
#         resp.content = dataJson
#         return resp
#     else:
#         return HttpResponseNotAllowed(['GET'], "Método inválido")