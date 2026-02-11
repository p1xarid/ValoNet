from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="pictures/", blank=True, null=True)

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return "/static/pictures/default-avatar.png"


class SocialLink(models.Model):
    SocialLink_CHOICES = [
        ("twitch", "Twitch"),
        ("youtube", "YouTube"),
        ("facebook", "Facebook"),
        ("twitter", "Twitter / X"),
        ("instagram", "Instagram"),
        ("discord", "Discord"),
    ]

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="social_links"
    )
    platform = models.CharField(max_length=20, choices=SocialLink_CHOICES)
    url = models.URLField()

    class Meta:
        unique_together = ("user", "platform")

    def __str__(self):
        return f"{self.user.username} - {self.platform}"


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
