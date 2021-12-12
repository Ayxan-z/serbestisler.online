from django.shortcuts import render
from blog.models import ArticleModel
from django.core.paginator import Paginator
from django.db.models import Q
#from IpBlock.ip_blocking import BlockedIpMiddleware

def homePage(request):
    search = request.GET.get('search')
    articles = ArticleModel.objects.order_by('-id')

    if search:
        articles = articles.filter(
            Q(title__icontains=search) |
            Q(content__icontains=search)
        ).distinct()
    
    page = request.GET.get('page')
    paginator = Paginator(articles, 3)

    return render(request, 'pages/homepage.html', context={
        'articles': paginator.get_page(page)
    })
    
