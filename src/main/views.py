from django.core.cache import cache
from rest_framework.viewsets import ModelViewSet

from .models import AmountOfUpvotes, Author, Comments
from .serializer import AmountOfUpvotesSerializer, AuthorSerializer, CommentsSerializer


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    cache_check = cache.get('author_cache')
    if not cache_check:
        cache_check = Author.objects.all()
        cache.set('author_cache', cache_check, 30)
    queryset = cache_check


class CommentsViewSet(ModelViewSet):
    serializer_class = CommentsSerializer
    cache_check = cache.get('comments_cache')
    if not cache_check:
        cache_check = Comments.objects.all()
        cache.set('comments_cache', cache_check, 30)
    queryset = cache_check


class AmountOfUpVotesViewSet(ModelViewSet):
    serializer_class = AmountOfUpvotesSerializer
    cache_check = cache.get('amounts_cache')
    if not cache_check:
        cache_check = AmountOfUpvotes.objects.all()
        cache.set('amounts_cache', cache_check, 30)
    queryset = cache_check
