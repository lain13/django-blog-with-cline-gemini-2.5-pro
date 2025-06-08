from django.urls import path
from ..views import category_views

urlpatterns = [
    path('category/<slug:slug>/', category_views.CategoryPostListView.as_view(), name='post_list_by_category'),
]
