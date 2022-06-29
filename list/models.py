from django.db import models

# Create your models here.
class Item(models.Model):
    cantidad = models.CharField(max_length=30)
    nombre = models.CharField(max_length=100)
    hecho = models.BooleanField()

    def __str__(self):
        return f'{self.cantidad} {self.nombre}'
