from django.test import TestCase
from ..models import Tag


class TagModelTest(TestCase):
    """Tag 모델 관련 테스트"""

    def test_tag_model_can_be_created(self):
        """Tag 모델 인스턴스가 올바르게 생성되는지 테스트"""
        # Given
        tag = Tag.objects.create(name="django")

        # When
        saved_tag = Tag.objects.get(pk=tag.pk)

        # Then
        self.assertEqual(saved_tag.name, "django")
