from django.shortcuts import render

# Create your views here.
# posts/views.py
from rest_framework import generics, permissions # new
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    #aca copiar es para realizar acciones aqui ejemplo seria en las boletas
    permission_classes = (permissions.IsAdminUser,) # new
    queryset = Post.objects.all()
    serializer_class = PostSerializer


