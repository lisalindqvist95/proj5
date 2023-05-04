from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Pin(models.Model):
    """
    Pin model, related to 'owner' and 'post'.
    'owner' is a User instance and 'post' is a Post instance.
    'unique_together' makes sure a user can't pin the same post twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='pins', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['post']

    def __str__(self):
        return f'{self.owner} {self.post}'