from turtle import mode
from django.db import models

# Create your models here.
class Persona(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    celular = models.BigIntegerField(default=0)

class Paciente(models.Model):
    numPaciente = models.AutoField(primary_key=True)
    idPaciente = models.ForeignKey(Persona, related_name="Paciente", on_delete=models.CASCADE) 
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    fechaNacimiento= models.DateField()

class Familiar(models.Model):
    numFamiliar = models.AutoField(primary_key=True)
    idFamiliar = models.ForeignKey(Persona, related_name="Familiar", on_delete=models.CASCADE)
    pacienteAsig = models.ForeignKey(Paciente, related_name="Paciente",on_delete=models.CASCADE)
    parentesco= models.CharField(max_length=45)
    correo = models.CharField(max_length=45)

class Doctor(models.Model):
    registro = models.SmallIntegerField(primary_key=True)
    especialidad = models.CharField(max_length=45)
    idDoctor = models.ForeignKey(Persona, related_name="Doctor", on_delete=models.CASCADE)

