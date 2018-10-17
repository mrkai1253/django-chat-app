from django import forms

from .models import MessageModel,Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = MessageModel
        fields = ['message']

class MsgForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['message']