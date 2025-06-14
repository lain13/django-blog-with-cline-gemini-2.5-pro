from django.contrib.auth.mixins import UserPassesTestMixin
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.author == request.user

class AuthorRequiredMixin(UserPassesTestMixin):
    """
    현재 로그인된 사용자가 객체의 작성자인지 확인하는 Mixin입니다.
    CBV(Create-Based View)에서 `self.get_object()`를 통해 얻어온 객체에
    `author` 속성이 존재하고, 그 값이 `request.user`와 동일한지 검사합니다.
    """
    def test_func(self):
        # get_object()는 UpdateView, DeleteView 등에서 객체를 가져오는 표준 메서드입니다.
        obj = self.get_object()
        return obj.author == self.request.user
