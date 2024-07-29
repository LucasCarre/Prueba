from django.shortcuts import render
from django.http import HttpResponse
from Appprueba.models import Curso
from Appprueba.forms import CursoFormulario, BuscaCursoForm

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

def formulario_curso(request):
    if request.method == 'POST':
        curso = Curso(nombre=request.POST['curso'], camada= request.POST['camada'])
        curso.save()
        return render(request, "appprueba/inicio.html")
    return render(request, 'appprueba/cursos.html')


def agregar_curso_api(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()

            return render(request, "appprueba/inicio.html")
    else:
        mi_formulario = CursoFormulario()

    return render(request, "appprueba/agregar-cursos-api.html", {"mi_formulario": mi_formulario})

def buscar_cursos(request):
    if request.method == "POST":
        mi_formulario = BuscaCursoForm(request.POST) # Aqui me llega la informacion del html

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])

            return render(request, "appprueba/mostrar_cursos.html", {"cursos": cursos})
    else:
        mi_formulario = BuscaCursoForm()

    return render(request, "appprueba/buscar_cursos.html", {"mi_formulario": mi_formulario})
