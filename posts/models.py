from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.now())
    content = models.TextField(max_length=1000000)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    comment = models.TextField(max_length=1000)
