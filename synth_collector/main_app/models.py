from django.db import models

# Create your models here.
class Synths(models.Model):

    name = models.CharField(max_length=100)
    maker = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    img = models.CharField(max_length=255)
    info = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Reviews(models.Model):

    review = models.TextField(max_length=500)
    like = models.BooleanField(None, default=False)
    synth = models.ForeignKey(Synths, on_delete=models.CASCADE, related_name='review')

    def __str__(self):
        return self.review

    def __bool__(self):
        return self.like


