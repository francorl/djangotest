from django.db import models

class User(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=10)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre
