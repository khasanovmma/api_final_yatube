from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
    )
    image = models.ImageField(upload_to="posts/", null=True, blank=True)
    group = models.ForeignKey(
        Group,
        related_name="posts",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    text = models.TextField()
    created = models.DateTimeField(
        "Дата добавления",
        auto_now_add=True,
        db_index=True,
    )


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="follower",
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="following"
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=~models.Q(user=models.F("following")),
                name="prevent_self_follow",
            ),
            models.UniqueConstraint(
                fields=["user", "following"],
                name="unique_follow",
            ),
        ]

    def __str__(self):
        return f"{self.user}"
