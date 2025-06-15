import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from ..models import Post, Vote

class VoteView(LoginRequiredMixin, View):
    """
    게시물 좋아요/싫어요에 대한 AJAX 요청을 처리합니다.
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
            # 이 사용자가 이 게시물에 대해 이미 투표한 경우
            vote = Vote.objects.get(user=request.user, post=post)
            if vote.value == vote_value:
                # 사용자가 같은 버튼을 다시 클릭하면 투표를 취소합니다.
                vote.delete()
            else:
                # 사용자가 투표를 변경하는 경우 (예: 좋아요에서 싫어요로)
                vote.value = vote_value
                vote.save()
        except Vote.DoesNotExist:
            # 투표가 존재하지 않으면 새로 생성합니다.
            Vote.objects.create(user=request.user, post=post, value=vote_value)

        post.refresh_from_db()
        user_vote = Vote.objects.filter(user=request.user, post=post).first()

        return JsonResponse({
            'like_count': post.like_count,
            'dislike_count': post.dislike_count,
            'liked': user_vote.value == Vote.LIKE if user_vote else False,
            'disliked': user_vote.value == Vote.DISLIKE if user_vote else False,
        })

    def handle_no_permission(self):
        return JsonResponse({'error': 'Authentication required'}, status=401)
