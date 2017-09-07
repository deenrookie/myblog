# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post
from .forms import PostForm
import markdown
# Create your views here.

# index page
def index(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')

# List of posts on homepage
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    for post in posts:
        post.text = markdown.markdown(post.text,
                         extesnsions=[
                         'markdown.extensions.extra',
                         'markdown.extensions.codehilite',
                         'markdown.extensions.toc',

        ])
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.text = markdown.markdown(post.text,
                         extesnsions=[
                         'markdown.extensions.extra',
                         'markdown.extensions.codehilite',
                         'markdown.extensions.toc',

    ])
    return render(request, 'blog/post_detail.html', {'post': post})