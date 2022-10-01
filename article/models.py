from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
  author = models.ForeignKey(User, on_delete = models.CASCADE)
  name = models.CharField(max_length = 100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ['name']

  def __str__(self):
    return self.name


class Post(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=230)
  content = models.TextField()
  tags = models.ManyToManyField(Tag)
  image = models.ImageField(upload_to ='uploads/')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ['title']

  def __str__(self):
    return self.title

class Comment(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, related_name='comment_set', on_delete=models.CASCADE)
  text = models.TextField()
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ['updated_at']

  def __str__(self):
    return self.text

