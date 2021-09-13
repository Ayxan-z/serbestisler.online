from blog import views
from django.urls import path

urlpatterns = [
    path('', views.homePage, name='homepage'),
    path('contact', views.contact, name='contact'),
    path('category/<slug:categorySlug>', views.category, name='category'),
    path('myarticles', views.myArticles, name='myarticles'),
]
