from django.contrib.auth.models import User
from django.db import models


class MessageModel(models.Model):
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver_name = models.CharField(max_length=128,default='receiver')
    sender_name = models.CharField(max_length=128,default='sender')
    message = models.TextField(max_length=256,default=None)

    def __str__(self):
        return '{0} to {1}'.format(self.sender_name,self.receiver.username)

class Message(models.Model):
    receiver_name = models.CharField(max_length=128,default='receiver')
    sender_name = models.CharField(max_length=128,default='sender')
    timestamp = models.DateTimeField(auto_now_add=True, editable=False, null=False, blank=False)
    message = models.CharField(max_length=128,default=None)

    def __str__(self):
        return '{0} to {1}'.format(self.sender_name,self.receiver_name)