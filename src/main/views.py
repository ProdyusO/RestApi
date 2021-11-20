from rest_framework.viewsets import ModelViewSet

from .models import AmountOfUpvotes, Author, Comments
from .serializer import AmountOfUpvotesSerializer, AuthorSerializer, CommentsSerializer


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class CommentsViewSet(ModelViewSet):
    serializer_class = CommentsSerializer
    queryset = Comments.objects.all()


class AmountOfUpVotesViewSet(ModelViewSet):
    serializer_class = AmountOfUpvotesSerializer
    queryset = AmountOfUpvotes.objects.all()
