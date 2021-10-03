from django.shortcuts import get_object_or_404
from blog.models import ArticleModel
from django.views.generic import UpdateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class UpdateArticleUpdateView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    template_name = 'pages/update-article.html'
    fields = ('title', 'content', 'image', 'categories')
    
    def get_object(self):
        article = get_object_or_404(ArticleModel,slug=self.kwargs.get('slug'),author=self.request.user)
        
        return article

    def get_success_url(self):
        return reverse('detail', kwargs={'slug': self.get_object().slug})

