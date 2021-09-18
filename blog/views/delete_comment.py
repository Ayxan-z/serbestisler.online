from django.contrib.auth.decorators import login_required
from blog.models import CommentModel
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

@login_required(login_url='/')
def delete_comment(request, id):
    comment = get_object_or_404(CommentModel, id=id)

    if comment.author == request.user or comment.article.author == request.user:
        comment.delete()
        
        messages.success(request, 'Commnent deleted')
        return redirect('detail', slug=comment.article.slug)
    
    return redirect('homepage')
    
