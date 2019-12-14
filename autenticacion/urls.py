from django.urls import path
from .import views

urlpatterns = [
    path("LOGIN", views.LOGIN, name="LOGIN"),
    path("LOGOUT", views.LOGOUT, name="LOGOUT"),
    path("REGISTERR", views.REGISTERR, name="REGISTERR"),
]
