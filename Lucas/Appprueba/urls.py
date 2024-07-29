from django.urls import path
from Appprueba import views

urlpatterns = [
    path('/', views.inicio, name='Inicio'),
    path('cursos/', views.cursos, name='Cursos'),
    path('profesores/', views.profesores, name= 'Profesores'),
    path('estudiantes/', views.estudiantes, name='Estudiantes'),
    path('practicas/', views.practicas, name= 'Practicas')
]