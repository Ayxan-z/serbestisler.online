from blog import views
from django.urls import path

urlpatterns = [
    path('', views.homePage, name='homepage'),
    path('contact', views.contact, name='contact'),
]
