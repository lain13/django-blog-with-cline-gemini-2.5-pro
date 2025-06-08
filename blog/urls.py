from django.urls import path, include

urlpatterns = [
    path('', include('blog.urls.post_urls')),
    path('', include('blog.urls.comment_urls')),
]
