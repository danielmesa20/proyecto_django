from django.contrib import admin
from productos.models import Productos

# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display = ("nombre","precio","cant_disp","categoria","image")
    search_fields = ("nombre","precio","cant_disp","categoria","image")

admin.site.register(Productos,ClientesAdmin)