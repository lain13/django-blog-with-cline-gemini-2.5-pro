from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView
from users.models import Profile
from users.forms import ProfileForm


class ProfileDetailView(DetailView):
    model = Profile
    slug_field = "user__username"
    slug_url_kwarg = "username"
    template_name = "users/profile_detail.html"
    context_object_name = "profile"


class ProfileUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "users/profile_form.html"

    def get_object(self, queryset=None):
        # URL의 username과 관계없이, 현재 로그인된 사용자의 프로필을 가져옵니다.
        return self.request.user.profile

    def test_func(self):
        # URL의 username과 로그인한 사용자의 username이 같은지 확인합니다.
        return self.kwargs.get("username") == self.request.user.username

    def get_success_url(self):
        return reverse_lazy(
            "users:profile_detail", kwargs={"username": self.request.user.username}
        )
