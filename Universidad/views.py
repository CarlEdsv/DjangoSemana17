from django.shortcuts import render
from .models import *

def carreraList(request):
    carreras = Carrera.objects.all()
    return render(request,"Carreras.html",{'carreras':carreras})

def profesorList(request):
    profesores = Profesor.objects.all()
    return render(request,"Profesores.html",{'profesores':profesores})

def estudianteList(request):
    estudiantes = Estudiante.objects.all()
    return render(request,"Estudiantes.html",{'estudiantes':estudiantes})

def asignaturaList(request):
    asignaturas = Asignatura.objects.all()
    return render(request,"Asignaturas.html",{'asignaturas':asignaturas})

# Create your views here.
