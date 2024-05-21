from django.urls import path
from . import views

app_name = "comments"

urlpatterns = [
    path("<pk>/delete", views.delete, name="delete"),
    path("<pk>/position", views.position, name="position"),
]
