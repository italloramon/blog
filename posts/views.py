from django.shortcuts import render, redirect
from .models import Post, Comment
from django.http import HttpResponse

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'post.html', {'post': post})

def comment(request):
    name = request.POST['name']
    comment = request.POST['comment']
    post_id = request.POST['post']
    post = Post.objects.get(id=int(post_id))
    
    com = Comment(name=name, comment=comment, post=post)
    com.save()

    return render(request, 'post.html', {'post': post})