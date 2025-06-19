from .auth_urls import urlpatterns as auth_urls

app_name = 'users'

urlpatterns = []
urlpatterns += auth_urls
