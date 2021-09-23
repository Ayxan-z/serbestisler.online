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
        
        if request.user.is_authenticated:
            logger.info('article read: ' + request.user.username)
        
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
            messages.success(request, 'Comment Added')
        
        return redirect('detail', slug=slug)
        
        
        
'''def detail(request, slug):
    article = get_object_or_404(ArticleModel, slug=slug)
    comments = article.comments.order_by('-id')
    
    if request.method == 'POST':
        add_comment_form = CommentAddModelForm(data=request.POST)
        if add_comment_form.is_valid():
            comment = add_comment_form.save(commit=False)
            comment.author = request.user
            comment.article = article
            comment.save()
            
    add_comment_form = CommentAddModelForm()
    
    return render(request, 'pages/detail.html', context={
        'article': article,
        'comments': comments,
        "add_comment_form": add_comment_form,
    })'''

