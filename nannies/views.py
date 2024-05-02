from django.shortcuts import HttpResponse, render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.decorators.http import require_POST
from .models import Nanny
from .forms import NannyForm
from comments.forms import CommentForm
from django.views.generic import FormView, ListView, DetailView, DeleteView


class IndexView(ListView):
    model = Nanny

    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.GET.get("keyword", "").strip()

        return queryset.filter(name__icontains=keyword)


class ShowView(DetailView):
    model = Nanny
    extra_context = {"comment_form": CommentForm()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comment_set.all().order_by("-id")
        return context

    def post(self, request, pk):
        nanny = self.get_object()
        form = NannyForm(request.POST, instance=nanny)

        if form.is_valid():
            form.save()
            messages.success(request, "更新成功")

        return redirect("nannies:show", pk=nanny.id)


class NewView(FormView):
    form_class = NannyForm
    template_name = "nannies/new.html"


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


class NannyDeleteView(DeleteView):
    model = Nanny

    def get_success_url(self):
        messages.success(self.request, "已刪除")
        return reverse("nannies:index")
