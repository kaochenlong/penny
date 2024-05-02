from django import forms
from django.forms import ModelForm, widgets
from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        labels = {"content": "留言內容"}
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "rows": 4,
                    "class": "textarea textarea-bordered",
                }
            )
        }
