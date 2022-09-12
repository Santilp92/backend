from django.db import models



# Create your models here.
class Persona(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    celular = models.BigIntegerField(default=0)

class Paciente(Persona):
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    fechaNacimiento= models.DateField()

class Familiar(Paciente):
    parentesco= models.CharField(max_length=45)
    correo = models.CharField(max_length=45)

class Doctor(Persona):
    registro = models.SmallIntegerField(unique=True)
    especialidad = models.CharField(max_length=45)

