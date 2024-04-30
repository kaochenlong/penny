from django.urls import path
from . import views
from .views import NewView, IndexView, ShowView, NannyDeleteView

app_name = "nannies"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("new", NewView.as_view(), name="new"),
    path("add", views.create, name="add"),
    path("<id>/edit", views.edit, name="edit"),
    path("<pk>/delete", NannyDeleteView.as_view(), name="delete"),
    path("<pk>", ShowView.as_view(), name="show"),
]
