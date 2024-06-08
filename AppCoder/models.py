from django.db import models

# Create your models here.
class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.camada}'

class Estudiante(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(null=True)
   
class Profesor(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

class Entregable(models.Model):

    nombre = models.CharField(max_length=40)
    fechaDeEntrega = models.DateField()
    entregado =models.BooleanField()

class EventoEscolar(models.Model):

    nombre = models.CharField(max_length=40)
    fecha = models.DateField()
    descripcion = models.CharField(max_length=30)

class Calificacion(models.Model):

    estudiante = models.CharField(max_length=40)
    curso = models.CharField(max_length=40)
    nota = models.IntegerField()

class ActividadRecreativa(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=30)
    fecha = models.DateField()