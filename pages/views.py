from django.shortcuts import render


def home(request):
    return render(request, "pages/home.html")


def about_us(request):
    return render(request, "pages/about.html")
