from django.shortcuts import render
from django.http import HttpResponse

def friends_view(request):
    # how to get friends list from database
    # in which HTML should we render this friends list
    return HttpResponse("Friends")

def blog_view(request):
    # how to get posts from database
    # in which HTML should we render this posts 
    return HttpResponse("<h1>Blog</h1>")

