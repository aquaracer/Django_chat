from django.db import models
from django.contrib.auth.models import User


class Messages(models.Model):
    messages = models.CharField(max_length=256)
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    #type = models.TextChoices()

