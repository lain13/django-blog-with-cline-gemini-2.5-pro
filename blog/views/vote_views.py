import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models import Post, Vote

class VoteView(LoginRequiredMixin, View):
    """
    Handle AJAX requests for liking/disliking a Post.
    """
    def post(self, request, *args, **kwargs):
        if not request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'error': 'Invalid request'}, status=400)

        post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        value = json.loads(request.body).get('value', None)
        
        if value not in ['like', 'dislike']:
            return JsonResponse({'error': 'Invalid vote value'}, status=400)

        vote_value = Vote.LIKE if value == 'like' else Vote.DISLIKE
        
        try:
            # If a vote from this user for this post already exists
            vote = Vote.objects.get(user=request.user, post=post)
            if vote.value == vote_value:
                # If the user clicks the same button again, cancel the vote
                vote.delete()
            else:
                # If the user changes their vote (e.g., from like to dislike)
                vote.value = vote_value
                vote.save()
        except Vote.DoesNotExist:
            # If no vote exists, create a new one
            Vote.objects.create(user=request.user, post=post, value=vote_value)

        post.refresh_from_db()
        user_vote = Vote.objects.filter(user=request.user, post=post).first()

        return JsonResponse({
            'vote_count': post.get_vote_count(),
            'liked': user_vote.value == Vote.LIKE if user_vote else False,
            'disliked': user_vote.value == Vote.DISLIKE if user_vote else False,
        })

    def handle_no_permission(self):
        return JsonResponse({'error': 'Authentication required'}, status=401)
