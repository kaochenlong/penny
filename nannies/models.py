from django.db import models
from django.utils import timezone


class NannyManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at=None)


class Nanny(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    tel = models.CharField(max_length=20)
    nickname = models.CharField(max_length=100)
    description = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True)

    objects = NannyManager()

    def __str__(self):
        gender_str = "Mr." if self.gender == "M" else "Mrs."
        return f"{gender_str} {self.name}"

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()
