from typing import Text
from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(max_length=100)
    name_surname = forms.CharField(max_length=30)
    message = forms.CharField(widget=forms.Textarea)
