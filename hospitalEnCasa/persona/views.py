from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def consultarPaciente(request):
    return HttpResponse("Consultar paciente")

def newMember(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            #print(data)
            #print(type(data))
            member = Members(
                name = data["name"],
                email = data["email"]
            )
            #print(member)
            member.save()
            return HttpResponse("Va a agragar un nuevo miembro")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['POST'], "Método inválido")

def getMember(request):
    if request.method == 'GET':
        members = Members.objects.all()
        allMemberData = []
        for x in members:
            data = {"id": x.id, "name": x.name, "email":x.email}
            allMemberData.append(data)
        dataJson = json.dumps(allMemberData)
        #print(dataJson)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")