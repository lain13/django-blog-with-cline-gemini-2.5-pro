from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView
from ..models import Post, Comment
from .. import forms

class CommentCreateView(CreateView):
    model = Comment
    form_class = forms.CommentForm

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.post = post
        form.instance.author = "Test Author" # 임시 하드코딩
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.kwargs['pk']})
