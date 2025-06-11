from django.test import TestCase
from ..models import Category


class CategoryModelTest(TestCase):
    """Category 모델 관련 테스트"""

    def test_category_model_can_be_created(self):
        """Category 모델 인스턴스가 올바르게 생성되는지 테스트"""
        # Given
        category = Category.objects.create(name="Programming", slug="programming")

        # When
        saved_category = Category.objects.get(pk=category.pk)

        # Then
        self.assertEqual(saved_category.name, "Programming")
        self.assertEqual(saved_category.slug, "programming")

    def test_category_str_representation(self):
        """Category 모델의 __str__ 메서드가 올바르게 동작하는지 테스트"""
        # Given
        category = Category.objects.create(name="Life", slug="life")

        # When/Then
        self.assertEqual(str(category), "Life")

    def test_hierarchical_category(self):
        """계층형 카테고리 관계가 올바르게 설정되는지 테스트"""
        # Given
        parent_category = Category.objects.create(name="Tech", slug="tech")
        child_category = Category.objects.create(
            name="Python",
            slug="python",
            parent=parent_category
        )

        # When
        saved_child = Category.objects.get(pk=child_category.pk)

        # Then
        self.assertIsNotNone(saved_child.parent)
        self.assertEqual(saved_child.parent, parent_category)
        self.assertIn(child_category, parent_category.children.all())
