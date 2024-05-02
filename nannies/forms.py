from django import forms
from django.forms import widgets
from .models import Nanny


class NannyForm(forms.ModelForm):
    class Meta:
        model = Nanny
        fields = ["name", "gender", "tel", "nickname", "description"]
        labels = {
            "name": "姓名",
            "gender": "性別",
            "tel": "電話",
            "nickname": "暱稱",
            "description": "簡介",
        }
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "input input-bordered"},
            ),
            "tel": forms.TextInput(
                attrs={"class": "input input-bordered"},
            ),
            "gender": forms.Select(
                attrs={"class": "select select-bordered"},
            ),
            "nickname": forms.TextInput(
                attrs={"class": "input input-bordered"},
            ),
            "description": forms.Textarea(
                attrs={"class": "textarea textarea-bordered"},
            ),
        }
