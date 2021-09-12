from blog import views
from django.urls import path

urlpatterns = [
    path('', views.homePage),
    path('contact', views.contact),
]
