from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Hello World <h1>")
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Hello World <h1>")
    return render(request, "about.html", {})

def eboard_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Hello World <h1>")
    return render(request, "eboard.html", {})

def gallery_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Hello World <h1>")
    return render(request, "gallery.html", {})

def donate_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Hello World <h1>")
    return render(request, "donate.html", {})

def meetings_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Hello World <h1>")
    return render(request, "meetings.html", {})