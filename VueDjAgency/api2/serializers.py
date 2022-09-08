# Serializers define the API representation.
from dataclasses import fields
from django.contrib.auth.models import User
from rest_framework import serializers
from blog.models import Category, Comment, Tag

from blog.models import Post

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class PostListSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    class Meta:
        model = Post
        fields = ['id','title','image','like','category']

# class PostLikeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ['like']

class PostRetrieveSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    tags = serializers.StringRelatedField(many = True)
    
    class Meta:
        model = Post
        exclude = ['create_dt'] 

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CategorySerialzier(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields=['name']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class CateTagSerializer(serializers.Serializer):
    # cateList = CategorySerialzier(many=True)
    # tagList = TagSerializer(many = True)
    cateList = serializers.ListField(child = serializers.CharField())
    tagList = serializers.ListField(child = serializers.CharField())

class PostSerializerSub(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title']

class CommentSerializerSub(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','content','update_dt']


class PostDetailSerializer(serializers.Serializer):
    post = PostRetrieveSerializer()
    prevPost = PostSerializerSub()
    nextPost = PostSerializerSub()
    commentList = CommentSerializerSub(many=True)