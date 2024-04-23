from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="root"),
    path("about", views.about_us, name="about"),
]
