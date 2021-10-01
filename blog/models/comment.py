from django.db import models
from blog.models import ArticleModel
from blog.models.abstract_models import DateAbstractModel

class CommentModel(DateAbstractModel):
    author = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='comment')
    article = models.ForeignKey(ArticleModel, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(verbose_name='Şərh')
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        db_table = 'Comment'
    
    def __str__(self):
        return self.author.username
