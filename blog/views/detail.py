from django.shortcuts import get_object_or_404, render
from blog.models import ArticleModel

def detail(request, slug):
    article = get_object_or_404(ArticleModel, slug=slug)
    comments = article.comments.order_by('-id')
    
    return render(request, 'pages/detail.html', context={
        'article': article,
        'comments': comments,
    })

