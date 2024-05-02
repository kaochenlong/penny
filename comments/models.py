from django.db import models
from nannies.models import Nanny


class Comment(models.Model):
    nanny = models.ForeignKey(
        Nanny,
        on_delete=models.CASCADE,
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)
