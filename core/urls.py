from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("pages.urls")),
    path("nannies/", include("nannies.urls")),
    path("comments/", include("comments.urls")),
    path("hello_kitty/", admin.site.urls),
]
