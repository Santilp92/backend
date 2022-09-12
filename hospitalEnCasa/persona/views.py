from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
import json

from .models import Doctor, Paciente, Persona, Familiar


# Create your views here.

def buscarPaciente(request):
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
                persona_ptr_id = data["id"],
                registro = data["registro"],
                especialidad = data["especialidad"],
                )
            doctor.save()
            persona.save()
            return HttpResponse("Nuevo doctor agregadoo")
        except:
            return HttpResponseBadRequest("Error en los datos enviados de doctor")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def consultarPacientes(request):
    if request.method == 'GET':
        pacientes = Paciente.objects.all()
        print (type(pacientes))
        personas = Persona.objects.all()
        pacientesData = []
        for x in pacientes:
            fechaStr =x.fechaNacimiento.strftime("%Y-%m-%d",)
            data = {"direccion": x.direccion, "ciudad":x.ciudad,
            "fechaNacimiento":fechaStr}
            print(data)
            pacientesData.append(data)
        dataJson = json.dumps(pacientesData)
        #print(dataJson)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")