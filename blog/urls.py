from blog import views
from django.urls import path
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    path('', views.homePage, name='homepage'),
    path('about', TemplateView.as_view(
        template_name='pages/about.html'
        ), name='about'),
    # path('redirect', RedirectView.as_view(
    #     url='https://www.google.com'
    #     ), name='redirect'),
    path('contact', views.contact, name='contact'),
    path('category/<slug:categorySlug>', views.CategoryListView.as_view(), name='category'),
    path('myarticles', views.myArticles, name='myarticles'),
    path('detail/<slug:slug>', views.DetailView.as_view(), name='detail'),
    path('update-article/<slug:slug>', views.update_article, name='update-article'),
    path('delete-article/<slug:slug>', views.ArticleDeleteView.as_view(), name='delete-article'),
    path('delete-comment/<int:id>', views.delete_comment, name='delete-comment'),
    path('add-article', views.add_article, name='add-article'),
]
