from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, 'appprueba/inicio.html')

def cursos(request):
    return render(request, 'appprueba/cursos.html')

def profesores(request):
    return render(request, 'appprueba/profesores.html')

def estudiantes(request):
    return render(request, 'appprueba/estudiantes.html')

def practicas(request):
    return render(request, 'appprueba/practicas.html')