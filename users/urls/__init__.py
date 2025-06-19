from .auth_urls import urlpatterns as auth_urls
from .profile_urls import urlpatterns as profile_urls

app_name = 'users'

urlpatterns = []
urlpatterns += auth_urls
urlpatterns += profile_urls
