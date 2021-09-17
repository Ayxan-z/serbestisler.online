from django.shortcuts import render, redirect, get_object_or_404
from blog.forms import ArticleUpdateModelForm
from blog.models import ArticleModel
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def update_article(request, slug):
    article = get_object_or_404(ArticleModel, slug=slug, author=request.user)
    form = ArticleUpdateModelForm(request.POST or None, files=request.FILES or None, instance=article)
    
    if form.is_valid():
        form.save()
        return redirect('detail', slug=article.slug)
    
    return render(request, 'pages/update_article.html', context={"form": form})

