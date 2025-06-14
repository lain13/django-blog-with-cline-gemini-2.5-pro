from django.contrib.auth import get_user_model
from blog.models import Post, Category, Tag

def create_user(username="testuser", password="password"):
    """Helper function to create a user."""
    User = get_user_model()
    return User.objects.create_user(username=username, password=password)

def create_post(author, title="Test Post", content="Test Content", category=None, tags=None):
    """Helper function to create a post."""
    post = Post.objects.create(author=author, title=title, content=content, category=category)
    if tags:
        for tag_name in tags:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            post.tags.add(tag)
    return post

def create_category(name="Test Category", slug="test-category"):
    """Helper function to create a category."""
    return Category.objects.create(name=name, slug=slug)
