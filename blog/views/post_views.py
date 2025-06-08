from django.shortcuts import render, get_object_or_404, redirect
from ..models import Post, Tag
from .. import forms
from django.db.models import Q

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # Note: CommentForm is now handled in comment_views.py, but the detail view still needs to render the page.
    # The form itself will be handled by a separate view/template tag later if needed.
    comment_form = forms.CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'comment_form': comment_form})

def post_new(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = forms.PostForm()
    return render(request, 'blog/post_form.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = forms.PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = forms.PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'blog/post_confirm_delete.html', {'post': post})

def search(request):
    query = request.GET.get('q')
    context = {'query': query}

    if not query:
        context['message'] = "Please enter a search term."
        return render(request, 'blog/search_results.html', context)

    results = Post.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query) | Q(tags__name__icontains=query)
    ).distinct()

    if not results.exists():
        context['message'] = "No posts found."
    
    context['posts'] = results
    return render(request, 'blog/search_results.html', context)

def post_list_by_tag(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    posts = Post.objects.filter(tags=tag)
    return render(request, 'blog/post_list.html', {'posts': posts, 'tag': tag})
