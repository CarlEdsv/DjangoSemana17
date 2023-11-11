from django.db import models

# Create your models here.
class Carrera(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    
class Profesor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)

class Estudiante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    carreraid = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    
class Asignatura(models.Model):
    id = models.AutoField(primary_key=True)#Llave primaria
    nombre = models.CharField(max_length=100)
    carreraid = models.ForeignKey(Carrera, on_delete=models.CASCADE)#Llave foránea
    profesorid = models.ForeignKey(Profesor, on_delete=models.CASCADE)#LLave foránea