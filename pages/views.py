from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "pages/home.html"


class AboutUsView(TemplateView):
    template_name = "pages/about.html"
