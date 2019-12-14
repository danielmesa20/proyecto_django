from django.shortcuts import render
from productos.models import Productos

# Create your views here.

def HOME(request):
     base = Productos.objects.filter(categoria="Base")
     labial = Productos.objects.filter(categoria="Labiales")
     return render(request, "home.html",{"base": base, "labial": labial})

def STORE(request, filtro=None):
     if filtro == 0:
          products = Productos.objects.all()
     elif filtro == 1:
          products= Productos.objects.filter(categoria="Base")
     return render(request, "tienda.html", {"products": products})
    
def FAVORITE(request):
     if not request.user.is_authenticated:
         print("eror")
     else:
          print("no error")
     return render(request, "tienda.html")