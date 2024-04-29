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

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()
