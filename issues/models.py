from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.auth.models import AbstractUser


class Status(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Issue(models.Model):
    name = models.CharField(max_length=64)
    summary = models.CharField(max_length=128)
    description = models.TextField(default="No description provided")
    reporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    assignee = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="assignee",
        blank=True, null=True
    )
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy("detail", args=[self.id])


# Create your models here.
