from django.shortcuts import render
from django.views.generic import TemplateView
from nannies.models import Nanny


class HomeView(TemplateView):
    template_name = "pages/home.html"


class AboutUsView(TemplateView):
    template_name = "pages/about.html"


def user_list(request):
    nannies = Nanny.objects.all()
    return render(request, "pages/user_list.html", {"nannies": nannies})
