from django.shortcuts import render, redirect
from productos.models import Productos

# Create your views here.

def HOME(request):
     return render(request, "home.html")

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

def add_cart(self,cantidad):
     print("cantidad")
     print(cantidad)
     return redirect("/productos/STORE/1")