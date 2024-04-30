from django.urls import path
from .views import HomeView, AboutUsView, user_list

urlpatterns = [
    path("", HomeView.as_view(), name="root"),
    path("about", AboutUsView.as_view(), name="about"),
    path("api/user_list", user_list),
]
