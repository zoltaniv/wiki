from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.read_entry, name="read_entry"),
    path("wiki/random/", views.random_page, name="random_page")
]
