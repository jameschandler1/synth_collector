from django.db import models 
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Synth(models.Model):

    synth_user = models.ManyToManyField(User, serialize=True)
    name = models.CharField(max_length=100)
    maker = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    img = models.CharField(max_length=200, default=None, null=True)
    info = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

class Comment(models.Model):

    sfk = models.ForeignKey(Synth, on_delete=models.CASCADE, null=True, serialize=True, related_name='sfk')
    comment_user = models.OneToOneField(User, on_delete=models.CASCADE, serialize=True, null=True)
    comment_body = models.TextField(max_length=140, blank=True)
    comment_like = models.BooleanField(null=True)
    comment_created = models.DateTimeField(default=timezone.now) 
    reply_from = models.ManyToManyField(User, serialize=True, related_name='reply_from')

    def __num__(self):
        return self.pk

class Reply(models.Model):

    reply_user = models.OneToOneField(User, on_delete=models.CASCADE, serialize=True, null=True)
    reply_body = models.TextField(max_length=140, blank=True)
    reply_like = models.BooleanField(null=True)
    reply_created = models.DateTimeField(default=timezone.now)
    cid = models.ForeignKey(Comment, on_delete=models.PROTECT, serialize=True, related_name='comment', null=True)

    def __num__(self):
        return self.pk













