from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AmountOfUpVotesViewSet, AuthorViewSet, CommentsViewSet


router = DefaultRouter()
router.register('author', AuthorViewSet)
router.register('comment', CommentsViewSet)
router.register('amount_of_upvotes', AmountOfUpVotesViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]
