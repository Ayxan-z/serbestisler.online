from django.urls import path
from account import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', auth_views.LoginView.as_view(
        template_name = 'pages/login.html'
        ), name='login'),
    path('logout', views.logout_def, name='logout'),
    path('change-password', views.change_password, name='change-password'),
    path('profile-editing', views.profile_editing, name='profile-editing'),
    path('register', views.register, name='register'),
    path('user/<str:username>', views.ProfileDetailView.as_view(), name='profile')
]

