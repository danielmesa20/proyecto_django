from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.FloatField()
    cant_disp = models.IntegerField()
    categoria = models.CharField(max_length=30)
