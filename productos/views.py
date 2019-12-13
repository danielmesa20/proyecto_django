from django.shortcuts import render
from productos.models import Productos

# Create your views here.

def HOME(request):
     products = Productos.objects.all()
     return render(request, "home.html",{"products": products})

def STORE(request):
     products = Productos.objects.all()
     return render(request, "tienda.html")



# def INFO (request):
#      return render(request, "home.html", {"fecha": datetime.datetime.now()})