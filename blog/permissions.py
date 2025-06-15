from django.contrib.auth.mixins import UserPassesTestMixin
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    객체의 소유자만 수정할 수 있도록 하는 커스텀 권한입니다.
    """
    def has_object_permission(self, request, view, obj):
        # 읽기 권한은 모든 요청에 대해 허용되므로,
        # GET, HEAD, OPTIONS 요청은 항상 허용합니다.
        if request.method in permissions.SAFE_METHODS:
            return True

        # 쓰기 권한은 객체의 소유자에게만 부여됩니다.
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
