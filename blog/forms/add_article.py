from django import forms
from blog.models import ArticleModel

class ArticleAddModelForm(forms.ModelForm):
    class Meta:
        model = ArticleModel
        fields = ('title', 'image', 'content', 'categories')

