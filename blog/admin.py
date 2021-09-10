from django.contrib import admin
from blog import models
from blog.models import CategoryModel, ArticleModel

admin.site.register(CategoryModel)

class ArticleAdmin(admin.ModelAdmin):
    search_fields = (
        'title', 'content'
    )
    
    list_display = (
        'title', 'creation_date', 'arrangement_date'
    )

admin.site.register(ArticleModel, ArticleAdmin)

