from dataclasses import field
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Post, Tag, Comment

class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Group
    fields = ['url', 'name']

class CommmentSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Comment
    fields = '__all__'

class PostSerializer(serializers.HyperlinkedModelSerializer):
  tags = serializers.SlugRelatedField(
    many=True,
    read_only=True,
    slug_field='name'
  )
  comments = CommmentSerializer(source='comment_set', many=True)
  class Meta:
    model = Post
    fields = ['author','title','comments','content','tags','image','created_at', 'updated_at']

