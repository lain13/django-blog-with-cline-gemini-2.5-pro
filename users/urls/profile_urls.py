from django.urls import path
from users.views import profile_views

urlpatterns = [
    path('<str:username>/', profile_views.ProfileDetailView.as_view(), name='profile_detail'),
    path('<str:username>/edit/', profile_views.ProfileUpdateView.as_view(), name='profile_update'),
]
