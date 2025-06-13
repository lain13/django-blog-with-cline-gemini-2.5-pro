from django.urls import path, include
from django.contrib.auth import views as auth_views
from .. import views

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('api/', include('users.urls.api_urls')),
]
