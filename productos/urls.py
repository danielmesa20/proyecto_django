from django.urls import path
from .import views

urlpatterns = [
    path("STORE", views.STORE, name="STORE"),
]

