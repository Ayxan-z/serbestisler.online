from blog.models import ArticleModel
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    template_name = 'pages/article_deletion_confirmation.html'
    success_url = reverse_lazy('myarticles')
    
    def get_queryset(self):
        article = ArticleModel.objects.filter(slug=self.kwargs['slug'], author=self.request.user)
        return article
    

    
