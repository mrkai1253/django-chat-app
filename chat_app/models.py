from django.contrib.auth.models import User
from django.db import models


class MessageModel(models.Model):
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    sender_name = models.CharField(max_length=128,default='mrkai')
    message = models.TextField(max_length=256,default=None)

