from django.views.generic import DetailView
from users.models import Profile

class ProfileDetailView(DetailView):
    model = Profile
    slug_field = 'user__username'
    slug_url_kwarg = 'username'
    template_name = 'users/profile_detail.html'
    context_object_name = 'profile'
