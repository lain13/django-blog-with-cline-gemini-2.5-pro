from django.shortcuts import get_object_or_404, redirect
from ..models import Post
from .. import forms

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            # author 필드는 임시로 하드코딩합니다. 인증 기능 추가 시 수정 필요.
            comment.author = "Test Author"
            comment.save()
            return redirect('post_detail', pk=post.pk)
    return redirect('post_detail', pk=post.pk) # GET 요청 등 비정상 접근 시 상세페이지로 리다이렉트
