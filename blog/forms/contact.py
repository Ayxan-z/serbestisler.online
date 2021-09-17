from typing import Text
from django import forms
from blog.models import ContactModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ('name_surname', 'email', 'message')
