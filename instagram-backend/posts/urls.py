from django.urls import path, include
from rest_framework.routers import DefaultRouter

from posts.views import PostViewSet, LikeView, UserFeedView


router = DefaultRouter()
router.register('', PostViewSet)

app_name = 'posts'

urlpatterns = [
    path('feed/', UserFeedView.as_view(), name='feed'),
    path('like/<uuid:post_id>/', LikeView.as_view(), name='like'),
    path('', include(router.urls)),
]
