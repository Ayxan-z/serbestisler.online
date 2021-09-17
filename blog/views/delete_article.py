from django.contrib.auth.decorators import login_required
from blog.models import ArticleModel
from django.shortcuts import get_object_or_404, redirect

@login_required(login_url='/')
def delete_article(request, slug):
    get_object_or_404(ArticleModel, slug=slug, author=request.user).delete()

    return redirect('myarticles')
    
