from django.urls import path
from .import views

urlpatterns = [
    path("REGISTER", views.REGISTER, name="REGISTER"),
    path("LOGIN", views.LOGIN, name="LOGIN"),
    path("LOGOUT", views.LOGOUT, name="LOGOUT"),
]
