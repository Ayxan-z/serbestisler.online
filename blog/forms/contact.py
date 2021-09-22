from typing import Text
from django import forms
from blog.models import ContactModel
from django.core.mail import send_mail

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ('name_surname', 'email', 'message')

    def send_email(self, message):
        send_mail(
            subject='Formdan yeni mesaj var',
            message=message,
            from_email=None,
            recipient_list=['shahsuvarovayxan@gmail.com'],
            fail_silently=False
        )
