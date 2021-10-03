from django.views.generic import CreateView
from blog.models import ArticleModel
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class AddArticleCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    template_name = 'pages/add-article.html'
    model = ArticleModel
    fields = ('title','content','files','categories')
    
    def get_success_url(self):
        return reverse('detail', kwargs={
            'slug': self.object.slug
        })
    
    def form_valid(self, form):
        article = form.save(commit=False)
        article.author = self.request.user
        article.save()
        form.save_m2m()
        
        return super().form_valid(form)

