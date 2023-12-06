from django.db import models

# Create your models here.

class admins(models.Model):
    id_admin = models.AutoField(primary_key=True)
    nombre_admin = models.CharField(max_length=30)


class usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class articulos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_articulo = models.TextField(max_length=50)
    precio = models.IntegerField(max_length=4)
    descripcion = models.CharField(max_length=150)
