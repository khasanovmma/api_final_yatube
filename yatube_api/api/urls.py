from django.urls import path, include
from rest_framework import routers

from .views import (
    CommentViewSet,
    FollowViewSet,
    PostViewSet,
    GroupViewSet,
)


v1_router = routers.SimpleRouter()
v1_router.register("posts", PostViewSet, basename="post")
v1_router.register("groups", GroupViewSet, basename="groups")
v1_router.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comment"
)
v1_router.register("follow", FollowViewSet, basename="follow")

urlpatterns = [
    path("v1/", include(v1_router.urls)),
    path("v1/", include("djoser.urls.jwt")),
]
