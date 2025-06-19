from django.test import TestCase
from users.forms.profile_forms import ProfileForm
from users.models import User

class ProfileFormTest(TestCase):
    def test_profile_form_valid(self):
        """
        프로필 폼이 유효한 데이터로 검증되는지 테스트
        """
        user = User.objects.create_user(username='testuser', password='password123')
        form_data = {'bio': 'This is a test bio.'}
        form = ProfileForm(data=form_data, instance=user.profile)
        self.assertTrue(form.is_valid())

    def test_profile_form_fields(self):
        """
        프로필 폼이 올바른 필드를 가지고 있는지 테스트
        """
        user = User.objects.create_user(username='testuser', password='password123')
        form = ProfileForm(instance=user.profile)
        expected_fields = ['bio', 'avatar']
        self.assertEqual(list(form.fields.keys()), expected_fields)
