from django.db import models
from autoslug import AutoSlugField
from blog.models import CategoryModel
from ckeditor.fields import RichTextField, RichTextField
from blog.models.abstract_models import DateAbstractModel

class ArticleModel(DateAbstractModel):
    # image = models.ImageField('Şəkil', upload_to="article_image")
    files = models.FileField('Fayl', upload_to='files')
    title = models.CharField('Başlıq',max_length=50)
    content = RichTextField('Açıqlama')
    slug = AutoSlugField(populate_from='title', unique=True)
    categories = models.ManyToManyField(CategoryModel, related_name='article', verbose_name='Kateqoriyalar')
    author = models.ForeignKey('account.CustomUserModel', on_delete=models.CASCADE, related_name='articles')
    
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        db_table = 'Article'
    
    def __str__(self):
        return self.title
    
    