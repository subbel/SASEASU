from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Hello World <h1>")
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    return HttpResponse("<h1> Hello World <h1>")

def eboard_view(request, *args, **kwargs):
    return HttpResponse("<h1> Hello World <h1>")

def gallery_view(request, *args, **kwargs):
    return HttpResponse("<h1> Hello World <h1>")

def donate_view(request, *args, **kwargs):
    return HttpResponse("<h1> Hello World <h1>")

def meetings_view(request, *args, **kwargs):
    return HttpResponse("<h1> Hello World <h1>")