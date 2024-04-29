from django import forms
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
