from django.contrib import admin
from blog import models
from blog.models import CategoryModel, ArticleModel, CommentModel, ContactModel

# CategoryModel **********************************************
admin.site.register(CategoryModel)

# ArticleModel **********************************************
class ArticleAdmin(admin.ModelAdmin):
    search_fields = (
        'title', 'content'
    )
    
    list_display = (
        'title', 'creation_date', 'arrangement_date'
    )

admin.site.register(ArticleModel, ArticleAdmin)

# CommentModel **********************************************
class CommentAdmin(admin.ModelAdmin):
    search_fields = (
        'author__username',
    )
    list_display = (
        'author', 'creation_date', 'arrangement_date'
    )

admin.site.register(CommentModel, CommentAdmin)

# ContactModel **********************************************
class ContactAdmin(admin.ModelAdmin):
    search_fields = (
        'email',
    )
    list_display = (
        'email', 'creation_date'
    )

admin.site.register(ContactModel, ContactAdmin)
