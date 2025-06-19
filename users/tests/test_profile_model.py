from django.test import TestCase
from django.contrib.auth import get_user_model
from users.models import Profile

User = get_user_model()

class ProfileModelTest(TestCase):
    """
    Profile 모델에 대한 테스트 클래스
    """

    def test_profile_model_exists(self):
        """
        Profile 모델이 존재하는지 테스트
        """
        # 이 테스트는 이제 Profile 모델을 직접 임포트하므로 항상 통과해야 합니다.
        pass

    def test_user_creation_creates_profile(self):
        """
        User 생성 시 Profile이 자동으로 생성되는지 테스트
        """
        user = User.objects.create_user(username='testuser', password='password123')
        self.assertTrue(hasattr(user, 'profile'))
        self.assertIsInstance(user.profile, Profile)
