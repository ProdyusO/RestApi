from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AmountOfUpvotesVievSet, AuthorViewSet, CommentsViewSet


router = DefaultRouter()
router.register('author', AuthorViewSet)
router.register('comment', CommentsViewSet)
router.register('amount_of_upvotes', AmountOfUpvotesVievSet)


urlpatterns = [
    path('api/', include(router.urls)),
]
