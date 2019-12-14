from django.shortcuts import render
from productos.models import Productos

# Create your views here.

def HOME(request):
     products = Productos.objects.all()
     return render(request, "home.html",{"products": products})

def STORE(request, filtro=None):
     if filtro == 0:
          products = Productos.objects.all()
     elif filtro == 1:
          products= Productos.objects.filter(categoria="Base")
     return render(request, "tienda.html", {"products": products})
    
