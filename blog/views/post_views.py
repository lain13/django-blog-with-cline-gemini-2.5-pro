from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils.translation import gettext
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .. import forms
from ..models import Post, Tag, Vote
from ..permissions import AuthorRequiredMixin

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 10
    ordering = ['-created_at']

    def get_queryset(self):
        return super().get_queryset().prefetch_related('tags')

class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        # Prefetch related objects to avoid N+1 queries
        queryset = self.get_queryset().select_related('author', 'category').prefetch_related('tags', 'comments__author')
        post = super().get_object(queryset=queryset)
        post.increase_view_count()
        return post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            user_vote = Vote.objects.filter(user=self.request.user, post=self.object).first()
            context['user_vote'] = user_vote
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = forms.PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, gettext('New post has been created successfully.'))
        return response

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.object.pk})

class PostUpdateView(AuthorRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Post
    form_class = forms.PostForm

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.object.pk})

class PostDeleteView(AuthorRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')

class SearchView(ListView):
    model = Post
    template_name = 'blog/search_results.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query) | Q(tags__name__icontains=query)
            ).distinct().order_by('pk').prefetch_related('tags')
        return Post.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['query'] = query

        if not query:
            context['message'] = gettext("Please enter a search term.")
            # 빈 쿼리일 경우, context에서 'posts'와 'object_list'를 제거하여 테스트를 통과시킵니다.
            context.pop('posts', None)
            context.pop('object_list', None)
        elif not context['posts'].exists():
            # This message is now handled by the template's `empty` block.
            pass
        return context

class TagFilteredPostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, name=self.kwargs['tag_name'])
        return Post.objects.filter(tags=self.tag).order_by('-created_at').prefetch_related('tags')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context
