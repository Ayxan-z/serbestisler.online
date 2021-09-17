from django import forms
from blog.models import CommentModel

class CommentAddModelForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('comment',)

