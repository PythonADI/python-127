from django.shortcuts import render
from django.http import HttpResponse

def login_view(request):
    return HttpResponse("<h1>Login</h1>")

def logout_view(request):
    return render(request, "logout.html")