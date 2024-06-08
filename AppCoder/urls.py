from django.urls import path
from AppCoder.views import curso, lista_cursos, inicio, cursos, profesores, estudiantes, entregables, eventoescolar, calificacion, actividadrecreativa

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('lista-cursos/', lista_cursos),
    path('', inicio, name='Inicio'),
    path('cursos/', cursos, name='Cursos'),
    path('profesores/', profesores, name='Profesores'),
    path('estudiantes/', estudiantes, name='Estudiantes'),
    path('entregables/', entregables, name='Entregables'),
    path('eventoescolar/', eventoescolar, name='EventoEscolar'),
    path('calificacion/', calificacion, name='Calificacion'),
    path('actividadrecreativa/', actividadrecreativa, name='ActividadRecreativa'),
]
