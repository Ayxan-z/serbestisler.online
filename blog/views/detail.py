from django.shortcuts import get_object_or_404, render
from blog.models import ArticleModel
from blog.forms import CommentAddModelForm

def detail(request, slug):
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
    })

