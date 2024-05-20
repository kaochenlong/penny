from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_http_methods
from nannies.models import Nanny
from .forms import CommentForm
from .models import Comment
from django.http import HttpResponse, QueryDict, JsonResponse


@require_POST
def delete(req, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return HttpResponse("")


@require_POST
def create(req, pk):
    nanny = get_object_or_404(Nanny, pk=pk)

    form = CommentForm(req.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.nanny = nanny
        comment.save()

        # return redirect("nannies:show", pk=nanny.id)
        return render(req, "comments/comment.html", {"comment": comment})
    
@require_http_methods(["PATCH"])
def position(req, pk):
    comment = get_object_or_404(Comment, pk=pk)
    new_index = int(QueryDict(req.body)["newIndex"])
    comment.position = new_index
    comment.save()
    return JsonResponse({"status": "success", "newIndex": new_index})
    