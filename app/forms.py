from django import forms
from django.forms import ModelForm
from .models import *


class ChatMessageForm(ModelForm):
    body = forms.CharField(widget=forms.TextInput(attrs={"class":"h-full w-full rounded-full py-2 px-6", "rows":1, "placeholder":"Message..."}))
    class Meta:
        model = ChatMessage
        fields = ["body"]