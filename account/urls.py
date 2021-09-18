from django.urls import path
from account import views

urlpatterns = [
    path('logout', views.logout_def, name='logout')
]

