from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Post, Project

def index(request):
    template = loader.get_template("blog/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template("blog/about.html")
    context = {}
    return HttpResponse(template.render(context ,request))

def projects(request):
    latest_projects = Project.objects.order_by("-date")
    template = loader.get_template("blog/projects.html")
    context = {
        "latest_projects": latest_projects,
    }
    return HttpResponse(template.render(context, request))

def blog(request):
    latest_posts = Post.objects.order_by("-date")
    template = loader.get_template("blog/blog.html")
    context = {
        "latest_posts": latest_posts,
    }
    return HttpResponse(template.render(context, request))

def post(request, link):
    post = Post.objects.filter(link=link.strip())[0]
    template = loader.get_template("blog/post.html")
    context = {
        "post": post,
    }
    return HttpResponse(template.render(context, request))



