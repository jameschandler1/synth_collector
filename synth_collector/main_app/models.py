from django.db import models 
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Synth(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    maker = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    img = models.URLField(default=None, null=True)
    info = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

class Comment(Synth, models.Model):

    comment_user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    comment_body = models.TextField(max_length=140, blank=True)
    comment_like = models.BooleanField(null=True)
    comment_created = models.DateTimeField(default=timezone.now)
        
    def __num__(self):
        return self.pk

class Reply(Comment, models.Model):

    reply_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    reply_body = models.TextField(max_length=140, blank=True)
    reply_like = models.BooleanField(null=True)
    reply_created = models.DateTimeField(default=timezone.now)
    
    def __num__(self):
        return self.pk













