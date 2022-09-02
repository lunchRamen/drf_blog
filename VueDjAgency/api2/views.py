from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from api2.serializers import CommentSerializer
from blog.models import Comment
from api2.serializers import PostSerializer
from blog.models import Post
from api2.serializers import UserSerializer

from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView

# Create your views here.
# ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer