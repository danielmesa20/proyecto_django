from django.urls import path
from .import views

urlpatterns = [
    path("STORE/<int:filtro>", views.STORE, name="STORE"),
]

