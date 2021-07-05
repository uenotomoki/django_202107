from django import forms
from .models import SnsMessageModel

class SnsMessageForm(forms.Form):
    message = forms.CharField(label='Message')

class SnsCommentForm(forms.Form):
    message = forms.CharField(label='Message')