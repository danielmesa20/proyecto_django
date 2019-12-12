from django.shortcuts import render

# Create your views here.

def HOME(request):
     return render(request, "home.html")

def INFO(request):
     return render(request, "test.html")

# def INFO (request):
#      return render(request, "home.html", {"fecha": datetime.datetime.now()})