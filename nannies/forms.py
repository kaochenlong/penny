from django import forms


class NannyForm(forms.Form):
    name = forms.CharField(label="姓名", max_length=100)
    gender = forms.CharField(label="性別", max_length=1)
    tel = forms.CharField(label="電話", max_length=20)
    nickname = forms.CharField(label="暱稱", max_length=100)
    description = forms.CharField(label="簡介", widget=forms.Textarea)
