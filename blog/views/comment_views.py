from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from ..forms import CommentForm
from ..models import Comment, Post
from ..permissions import AuthorRequiredMixin

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

class CommentUpdateView(AuthorRequiredMixin, LoginRequiredMixin, UpdateView):
    """댓글 수정 뷰"""
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.object.post.pk})

class CommentDeleteView(AuthorRequiredMixin, LoginRequiredMixin, DeleteView):
    """댓글 삭제 뷰"""
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.object.post.pk})
