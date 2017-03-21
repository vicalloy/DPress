# -*- coding: UTF-8 -*-
from django.shortcuts import render, get_object_or_404

from taggit.models import Tag

from .models import Post
from .helper import archive_month_filter

def index(request, username=None, tag=None, year=None, month=None,
        category=None, template_name="dpress/index.html"):
    posts = Post.objects.filter(status=2)
    ctx = {}
    if tag:
        ctx['tag'] = get_object_or_404(Tag, name=tag)
        posts = posts.filter(tags__name__in=[tag])
    if year and month:
        posts, t_context = archive_month_filter(year, month, posts, 'publish')
        ctx.update(t_context)

    if category:
        posts = posts.filter(category__slug=category)

    if username:
        posts = posts.filter(author__username=username)
    posts = posts.order_by("-publish")
    ctx['posts'] = posts
    return render(request, template_name, ctx)

def post(request, year, month, slug,
         template_name="dpress/post.html"):
    post = get_object_or_404(Post, slug=slug, publish__year=int(year),
            publish__month=int(month), status=2)
    ctx = {}
    ctx['post'] = post
    return render(request, template_name, ctx)
