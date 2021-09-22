from django.views.generic import CreateView
from blog.models import ArticleModel
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class AddArticleCreateView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    template_name = 'pages/add-article.html'
    model = ArticleModel
    fields = ('title','content','image','categories')
    
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

'''@login_required(login_url='/')
def add_article(request):
    form = ArticleAddModelForm(request.POST or None, files=request.FILES or None)
    
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        form.save_m2m()
    
        return redirect('detail', slug=article.slug)
        
    return render(request, 'pages/add_article.html', context={"form": form})'''

