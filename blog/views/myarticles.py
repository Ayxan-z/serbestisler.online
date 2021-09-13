from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def myArticles(request):
    articles = request.user.articles.order_by('-id')
    page = request.GET.get('page')
    paginator = Paginator(articles, 1)

    return render(request, 'pages/myarticles.html', context={
        'articles': paginator.get_page(page),
    })
