from django.shortcuts import render
from blog.models import ArticleModel
from django.core.paginator import Paginator

def homePage(request):
    articles = ArticleModel.objects.order_by('-id')
    page = request.GET.get('page')
    paginator = Paginator(articles, 3)

    return render(request, 'pages/homepage.html', context={
        'articles': paginator.get_page(page)
    })

