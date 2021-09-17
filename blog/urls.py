from blog import views
from django.urls import path

urlpatterns = [
    path('', views.homePage, name='homepage'),
    path('contact', views.contact, name='contact'),
    path('category/<slug:categorySlug>', views.category, name='category'),
    path('myarticles', views.myArticles, name='myarticles'),
    path('detail/<slug:slug>', views.detail, name='detail'),
    path('update-article/<slug:slug>', views.update_article, name='update-article'),
    path('delete-article/<slug:slug>', views.delete_article, name='delete-article'),
    path('add-article', views.add_article, name='add-article'),
]
