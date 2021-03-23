from django.shortcuts import render, get_object_or_404
from .models import Post,Categories

# Create your views here.

def home(request):
    return render(request, 'home.html', {})

def blogs(request):
    all_posts = Post.newmanager.all()
    return render(request, 'index.html', {'posts' : all_posts})

def post_single(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    return render(request, 'single.html', {'post' : post})
