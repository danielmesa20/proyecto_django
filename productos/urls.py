from django.urls import path
from .import views

urlpatterns = [
    path("STORE/<int:filtro>", views.STORE, name="STORE"),
    path("FAVORITE", views.FAVORITE, name="FAVORITE"),
    path("add/<int:cantidad>", views.add_cart, name="add"),
]

