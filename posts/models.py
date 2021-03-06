from django.db import models
from django.contrib.auth import get_user_model
from companies.models import Company
from companies.models import compress


# Create your models here.

class Post(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=False, related_name='posts')
    description = models.TextField(blank=True)
    number_of_likes = models.PositiveIntegerField(default=0)
    number_of_dislikes = models.PositiveIntegerField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(get_user_model(), related_name='comments', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return '%s: %s' % (self.user, self.text)


class PostImages(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='post')

    def save(self, *args, **kwargs):
        self.image = compress(self.image, 40)
        super().save(*args, **kwargs)


class PostLikes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        unique_together = ['post', 'user']

    def __str__(self):
        return f'{self.user}: {self.post}'


class PostDislikes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        unique_together = ['post', 'user']

    def __str__(self):
        return f'{self.user}: {self.post}'
