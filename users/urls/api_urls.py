from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from ..views import api_views

app_name = 'users-api'

urlpatterns = [
    path('', api_views.UserListAPIView.as_view(), name='user-list-api'),
    path('<int:pk>/', api_views.UserDetailAPIView.as_view(), name='user-detail-api'),
    path('token/', obtain_auth_token, name='token_auth'),
]
