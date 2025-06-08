from .post_urls import urlpatterns as post_urls
from .comment_urls import urlpatterns as comment_urls

app_name = 'blog'

urlpatterns = []
urlpatterns += post_urls
urlpatterns += comment_urls
