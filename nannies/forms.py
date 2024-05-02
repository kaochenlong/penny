from django import forms
from django.forms import widgets
from .models import Nanny, GENDER_OPTIONS


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
            "gender": forms.Select(
                choices=GENDER_OPTIONS,
                attrs={"class": "px-2 py-1 border border-gray-500"},
            ),
        }
