from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
import json
from .models import Persona, Paciente, Doctor, Familiar


# Create your views here.
#----------------------
#funciones del auxiliar
#----------------------
def nuevaPersonaPaciente(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            persona = Persona(
                id = data["id"],
                nombres = data["nombres"],
                apellidos = data["apellidos"],
                celular = data["celular"]
                )
            persona.save()
            persona1 = Persona.objects.filter(id= data["id"]).first()
            if (not persona1):
                return HttpResponseBadRequest("No existe la persona con esa cédula")
            paciente = Paciente(
                idPaciente = persona1,
                direccion = data["direccion"],
                ciudad = data["ciudad"],
                fechaNacimiento = data["fechaNacimiento"]
                )
            paciente.save()
            return HttpResponse("Nuevo paciente agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def actualizarPersonaPaciente(request, id):
    if request.method == 'PUT':
        try:
            persona = Persona.objects.filter(id=id).first()
            if (not persona):
                return HttpResponseBadRequest("No existe la persona con esa cédula")
            data = json.loads(request.body)
            persona.celular = data["celular"]
            persona.save()

            paciente = Paciente.objects.filter(idPaciente = id).first()
            if (not paciente):
                return HttpResponseBadRequest("No existe el paciente")
            data = json.loads(request.body)
            paciente.direccion = data["direccion"]
            paciente.ciudad = data["ciudad"]
            paciente.save()
            return HttpResponse("Paciente actualizado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['PUT'], "Método inválido")

def consultarPersonasPacientes(request):
    if request.method == 'GET':   
        pacientes = Paciente.objects.all().values()
        if (not pacientes):
            return HttpResponseBadRequest("No hay paceintes en la bd")
        personasData = []
        for paciente in pacientes:
            idPaciente = paciente["idPaciente_id"]
            persona = Persona.objects.filter(id = idPaciente)
            for dato in persona:
                data = {"id":dato.id, "nombres": dato.nombres, 
                "apellidos":dato.apellidos}
                personasData.append(data)
                print(personasData)
         
        dataJson = json.dumps(personasData)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def borrarPersonaPaciente(request, id):
    if request.method == 'DELETE':
        try:
            paciente = Paciente.objects.filter(idPaciente=id).first()
            if (not paciente):
                return HttpResponseBadRequest("No existe pacientes con esta cédula")
            paciente.delete()

            persona = Persona.objects.filter(id=id).first()
            if (not persona):
                return HttpResponseBadRequest("No existe persona con esta cédula")
            persona.delete()
            return HttpResponse("Paciente eliminado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['DELETE'], "Método inválido")

def buscarPersonaPaciente(request, id):
    if request.method == 'GET':
        persona = Persona.objects.filter(id=id).first()
        if (not persona):
            return HttpResponseBadRequest("No existe paciente con esta cédula")
        
        paciente = Paciente.objects.filter(idPaciente = id)
        pacienteData = []
        for dato in paciente:
            fechaStr = dato.fechaNacimiento.strftime('%Y-%m-%d',)
            data = {"direccion":dato.direccion,"ciudad":dato.ciudad,
            "fechaNacimiento":fechaStr}
            pacienteData.append(data)
        data = {
            "id":persona.id, 
            "nombres": persona.nombres, 
            "apellidos":persona.apellidos, 
            "celular":persona.celular,
            "paciente":pacienteData
            }

        dataJson = json.dumps(data)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def nuevoFamiliar(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            PacienteAsi = data["idPaciente"]
            persona = Persona(
                id = data ["id"],
                nombres = data["nombres"],
                apellidos = data["apellidos"],
                celular = data["celular"],
                )
            persona.save()

            paciente = Paciente.objects.filter(idPaciente = PacienteAsi).first()
            persona = Persona.objects.filter(id= data["id"]).first()
            if (not persona):
                return HttpResponseBadRequest("No existe la persona con esa cédula")
            familiar = Familiar(
                idFamiliar = persona,
                pacienteAsig = paciente,
                parentesco = data["parentesco"],
                correo = ["correo"],
                )
            familiar.save()
            return HttpResponse("Nuevo familiar agregadoo")
        except:
            return HttpResponseBadRequest("Error en los datos enviados de familiar")
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
            persona.save()

            persona = Persona.objects.filter(id= data["id"]).first()
            if (not persona):
                return HttpResponseBadRequest("No existe la persona con esa cédula")
            doctor = Doctor(
                registro = data["registro"],
                especialidad = data["especialidad"],
                idDoctor = persona
                )
            
            doctor.save()
            return HttpResponse("Nuevo doctor agregadoo")
        except:
            return HttpResponseBadRequest("Error en los datos enviados de doctor")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

#----------------------
#Persona
#----------------------

def nuevaPersona(request):
    if request.method == 'POST':
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

def consultarPersonas(request):
    if request.method == 'GET':
        personas = Persona.objects.all()
        if (not personas):
            return HttpResponseBadRequest("No existen personas en la bd")
        personasData = []
        for x in personas:
            data = {"nombres": x.nombres, "apellidos":x.apellidos}
            personasData.append(data)
        dataJson = json.dumps(personasData)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

def buscarPersona(request, id):
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

def actualizarPersona(request, id):
    if request.method == 'PUT':
        try:
            persona = Persona.objects.filter(id=id).first()
            if (not persona):
                return HttpResponseBadRequest("No existe la persona con esa cédula")
            data = json.loads(request.body)
            persona.nombres = data["nombres"]
            persona.apellidos = data["apellidos"]
            persona.celular = data["celular"]
            persona.save()
            return HttpResponse("Persona actualizada")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['PUT'], "Método inválido")

def borrarPersona(request, id):
    if request.method == 'DELETE':
        try:
            persona = Persona.objects.filter(id=id).first()
            if (not persona):
                return HttpResponseBadRequest("No existe la persona con esa cédula")
            persona.delete()
            return HttpResponse("Persona eliminada")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['DELETE'], "Método inválido")

#----------------------
#Paciente
#----------------------
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
                direccion = data["direccion"],
                ciudad = data["ciudad"],
                fechaNacimiento = data["fechaNacimiento"]
                )
            persona.save()
            paciente.save()
            return HttpResponse("Nuevo paciente agregadoo")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def nuevoPaciente(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            persona = Persona.objects.filter(id= data["id"]).first()
            if (not persona):
                return HttpResponseBadRequest("No existe la persona con esa cédula")
            paciente = Paciente(
                idPaciente = persona,
                direccion = data["direccion"],
                ciudad = data["ciudad"],
                fechaNacimiento = data["fechaNacimiento"]
                )
            paciente.save()
            return HttpResponse("Nuevo paciente agregado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def actualizarPaciente(request, id):
    if request.method == 'PUT':
        try:
            paciente = Paciente.objects.filter(idPaciente = id).first()
            if (not paciente):
                return HttpResponseBadRequest("No existe el paciente")
            data = json.loads(request.body)
            paciente.direccion = data["direccion"]
            paciente.ciudad = data["ciudad"]
            paciente.save()
            return HttpResponse("Paciente actualizado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['PUT'], "Método inválido") 

def borrarPaciente(request, id):
    if request.method == 'DELETE':
        try:
            paciente = Paciente.objects.filter(idPaciente=id).first()
            if (not paciente):
                return HttpResponseBadRequest("No existe la persona con esa cédula")
            paciente.delete()
            return HttpResponse("Paciente eliminado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['DELETE'], "Método inválido")