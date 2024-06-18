from django.forms import ModelForm
from django import forms
from .models import *

class ChatmessageCreateForm(ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['body']
        labels = {
            'body': ''  # Itt távolítod el a címkét
        }
        widgets = {
            'body' : forms.TextInput(attrs={'placeholder': 'Üzenet küldése...' , 'class': 'p-4 text-dark w-100' , 'maxlength': '300' , 'autofocus': True})
        }