from django.shortcuts import render, redirect
from blog.forms import ArticleAddModelForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def add_article(request):
    form = ArticleAddModelForm(request.POST or None, files=request.FILES or None)
    
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        form.save_m2m()
    
        return redirect('detail', slug=article.slug)
        
    return render(request, 'pages/add_article.html', context={"form": form})

