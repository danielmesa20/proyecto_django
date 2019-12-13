from django.urls import path
from .import views

urlpatterns = [
    path("REGISTER", views.REGISTER, name="REGISTER"),
]
