from django.db import models


class Nanny(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    tel = models.CharField(max_length=20)
    nickname = models.CharField(max_length=100)
    description = models.TextField(default="")
