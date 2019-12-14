from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.FloatField()
    cant_disp = models.IntegerField()
    categoria = models.CharField(max_length=30)
    image = models.ImageField(upload_to='pics')

    def test(self):
        print("test")
        return reverse("add", kwargs={
            'cantidad': self.cant_disp
        })

#class Favoritos(models.Model):
    
    
   
