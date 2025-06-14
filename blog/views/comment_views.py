from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from ..forms import CommentForm
from ..models import Comment, Post

class AuthorRequiredMixin(UserPassesTestMixin):
    """작성자만 접근을 허용하는 믹스인"""
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class CommentCreateView(LoginRequiredMixin, CreateView):
    """댓글 생성 뷰"""
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.kwargs['pk']})

class CommentUpdateView(AuthorRequiredMixin, UpdateView):
    """댓글 수정 뷰"""
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.object.post.pk})

class CommentDeleteView(AuthorRequiredMixin, DeleteView):
    """댓글 삭제 뷰"""
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.object.post.pk})
