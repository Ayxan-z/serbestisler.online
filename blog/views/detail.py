from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from blog.models import ArticleModel
from blog.forms import CommentAddModelForm
from django.views import View
import logging

logger = logging.getLogger('article_read')

class DetailView(View):
    http_method_names = ['get', 'post']
    add_comment_form = CommentAddModelForm
    
    def get(self, request, slug):
        article = get_object_or_404(ArticleModel, slug=slug)
        
        articleRead = 'Unknown'
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
            
        if request.user.is_authenticated:
            articleRead = request.user.username
        logger.info(f'article: {article.title} article read: {articleRead} IP: {ip}')
        
        comments = article.comments.order_by('-id')

        return render(request, 'pages/detail.html', context={
        'article': article,
        'comments': comments,
        "add_comment_form": self.add_comment_form(),
        })
    
    def post(self, request, slug):
        article = get_object_or_404(ArticleModel, slug=slug)
        add_comment = self.add_comment_form(data=request.POST)
        
        if add_comment.is_valid():
            comment = add_comment.save(commit=False)
            comment.author = request.user
            comment.article = article
            comment.save()
            messages.success(request, 'Şərh əlavə olundu')
        
        return redirect('detail', slug=slug)

