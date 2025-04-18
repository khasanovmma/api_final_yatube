from django.urls import path, include
from rest_framework import routers


from .views import CommentViewSet, PostViewSet, GroupViewSet, JWTViewSet


v1_router = routers.SimpleRouter()
v1_router.register("posts", PostViewSet, basename="post")
v1_router.register("groups", GroupViewSet, basename="groups")
v1_router.register("jwt", JWTViewSet, basename="jwt")
v1_router.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comment"
)

urlpatterns = [
    path("v1/", include(v1_router.urls)),
]
