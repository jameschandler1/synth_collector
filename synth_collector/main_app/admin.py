from django.contrib import admin
from .models import Synth, Comment, Reply
# Register your models here.
admin.site.register(Reply)
admin.site.register(Synth)
admin.site.register(Comment)