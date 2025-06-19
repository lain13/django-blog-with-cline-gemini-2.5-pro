from django.urls import path
from django.contrib.auth import views as django_auth_views
from ..views import auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', django_auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', auth_views.SignUpView.as_view(), name='signup'),
]
