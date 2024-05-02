from django.urls import path
from . import views as nanny_views
from comments import views as comment_views
from .views import NewView, IndexView, ShowView, NannyDeleteView

app_name = "nannies"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("new", NewView.as_view(), name="new"),
    path("add", nanny_views.create, name="add"),
    path("<id>/edit", nanny_views.edit, name="edit"),
    path("<pk>/delete", NannyDeleteView.as_view(), name="delete"),
    path("<pk>/comment", comment_views.create, name="comment"),
    path("<pk>", ShowView.as_view(), name="show"),
]
