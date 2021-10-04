from django.shortcuts import get_object_or_404
from blog.models import CategoryModel
from django.views.generic import ListView

class CategoryListView(ListView):
    template_name = 'pages/category.html'
    context_object_name = 'articles'
    paginate_by = 5
    
    def get_queryset(self):
        category = get_object_or_404(CategoryModel, slug=self.kwargs['categorySlug'])
        return category.article.order_by('-id')

