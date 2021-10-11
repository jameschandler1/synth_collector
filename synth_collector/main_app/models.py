from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField # new

# Create your models here.
class Review(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=500)

    def __str__(self):
        return self.body
class Synth(models.Model):

    user = models.ManyToManyField(User)
    name = models.CharField(max_length=100)
    maker = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    img = models.CharField(max_length=255)
    info = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    review = models.ManyToManyField(Review)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
