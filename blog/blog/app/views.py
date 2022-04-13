from django.shortcuts import render
from .models import Post


def index(request):
    post = Post.objects.all()
    return render(request, 'index.html', {'posts': post})


def posts(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'posts.html', {'posts': posts})