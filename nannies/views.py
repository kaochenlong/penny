from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Nanny
from .forms import NannyForm


def index(request):
    nannies = Nanny.objects.all()
    return render(request, "nannies/index.html", {"nannies": nannies})


def show(request, id):
    nanny = get_object_or_404(Nanny, pk=id)

    if request.method == "POST":
        nanny.name = request.POST["name"]
        nanny.gender = request.POST["gender"]
        nanny.tel = request.POST["tel"]
        nanny.nickname = request.POST["nickname"]
        nanny.description = request.POST["description"]
        nanny.save()

        return redirect(f"/nannies/{nanny.id}")
    else:
        return render(request, "nannies/show.html", {"nanny": nanny})


def new(request):
    form = NannyForm()
    return render(request, "nannies/new.html", {"form": form})


def edit(request, id):
    nanny = get_object_or_404(Nanny, pk=id)
    return render(request, "nannies/edit.html", {"nanny": nanny})


@require_POST
def create(request):
    form = NannyForm(request.POST)

    if form.is_valid():
        Nanny.objects.create(**form.cleaned_data)

    return redirect("nannies:index")


@require_POST
def delete(request, id):
    nanny = get_object_or_404(Nanny, pk=id)
    nanny.delete()
    return redirect("nannies:index")
