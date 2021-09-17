from django.shortcuts import render, get_object_or_404
from blog.models import ArticleModel, CategoryModel
from django.core.paginator import Paginator

def category(request, categorySlug):
    category = get_object_or_404(CategoryModel, slug=categorySlug)
    articles = category.article.order_by('-id')
    page = request.GET.get('page')
    paginator = Paginator(articles, 3)

    return render(request, 'pages/category.html', context={
        'articles': paginator.get_page(page),
        'category_name': category.name
    })
