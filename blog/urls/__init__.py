from .post_urls import urlpatterns as post_urls
from .comment_urls import urlpatterns as comment_urls
from .category_urls import urlpatterns as category_urls
from .vote_urls import urlpatterns as vote_urls
from .feed_urls import urlpatterns as feed_urls

app_name = 'blog'

urlpatterns = []
urlpatterns += post_urls
urlpatterns += comment_urls
urlpatterns += category_urls
urlpatterns += vote_urls
urlpatterns += feed_urls
