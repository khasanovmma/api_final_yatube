from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Follow, Group, Post, Comment

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Post
        fields = ("id", "text", "pub_date", "image", "group", "author")


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "title", "slug", "description")


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(
        read_only=True,
        slug_field="username",
    )

    class Meta:
        model = Comment
        fields = ("id", "text", "created", "post", "author")
        read_only_fields = ("post",)


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)
    following = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ("user", "following")
        read_only_fields = ("user",)

    def validate(self, attrs):
        user = self.context["request"].user
        following_user = attrs.get("following")

        if user == following_user:
            raise serializers.ValidationError(
                "Нельзя подписаться на самого себя."
            )

        if Follow.objects.filter(user=user, following=following_user).exists():
            raise serializers.ValidationError(
                "Вы уже подписаны на этого пользователя."
            )

        return attrs
