from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Nanny
from .forms import NannyForm
from django.contrib import messages


def index(request):
    nannies = Nanny.objects.all()
    return render(request, "nannies/index.html", {"nannies": nannies})


def show(request, id):
    nanny = get_object_or_404(Nanny, pk=id)

    if request.method == "POST":
        form = NannyForm(request.POST, instance=nanny)

        if form.is_valid():
            form.save()
            messages.success(request, "更新成功")

        return redirect("nannies:show", id=nanny.id)
    else:
        return render(request, "nannies/show.html", {"nanny": nanny})


def new(request):
    form = NannyForm()
    return render(request, "nannies/new.html", {"form": form})


def edit(request, id):
    nanny = get_object_or_404(Nanny, pk=id)

    form = NannyForm(instance=nanny)

    return render(request, "nannies/edit.html", {"nanny": nanny, "form": form})


@require_POST
def create(request):
    form = NannyForm(request.POST)

    if form.is_valid():
        form.save()
        messages.success(request, "新增成功")

    return redirect("nannies:index")


@require_POST
def delete(request, id):
    nanny = get_object_or_404(Nanny, pk=id)
    nanny.delete()
    messages.error(request, "資料已刪除！")
    return redirect("nannies:index")
