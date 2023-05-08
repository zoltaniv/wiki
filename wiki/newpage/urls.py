from django.urls import path
from . import views

app_name = "newpage"

urlpatterns = [
    path("", views.index, name="index"),
    path("edit/<str:title>", views.edit, name="edit")
]