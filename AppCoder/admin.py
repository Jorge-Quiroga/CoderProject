from django.contrib import admin
from . models import Curso, Profesor, Estudiante, Entregable, EventoEscolar, Calificacion, ActividadRecreativa

# Register your models here.
admin.site.register(Curso)
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Entregable)
admin.site.register(EventoEscolar)
admin.site.register(Calificacion)
admin.site.register(ActividadRecreativa)