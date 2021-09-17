from django.contrib import admin
from blog import models
from blog.models import CategoryModel, ArticleModel, CommentModel, ContactModel

# CategoryModel **********************************************
admin.site.register(CategoryModel)

# ArticleModel **********************************************
@admin.register(ArticleModel)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = (
        'title', 'content'
    )
    
    list_display = (
        'title', 'creation_date', 'arrangement_date'
    )

# CommentModel **********************************************
@admin.register(CommentModel)
class CommentAdmin(admin.ModelAdmin):
    search_fields = (
        'author__username',
    )
    list_display = (
        'author', 'creation_date', 'arrangement_date'
    )

# ContactModel **********************************************
@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    search_fields = (
        'email',
    )
    list_display = (
        'name_surname','email', 'creation_date'
    )
