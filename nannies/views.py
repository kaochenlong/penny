from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_POST
from .models import Nanny


def index(request):
    nannies = Nanny.objects.all()
    return render(request, "nannies/index.html", {"nannies": nannies})


def new(request):
    return render(request, "nannies/new.html")


@require_POST
def create(request):
    nanny = Nanny(
        name=request.POST["name"],
        gender=request.POST["gender"],
        tel=request.POST["tel"],
        nickname=request.POST["nickname"],
        description=request.POST["description"],
    )
    nanny.save()

    return redirect(reverse("root"))
