from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from datetime import datetime

def index(request):
    now = datetime.now()

    return render(
        request,
        "HelloDjangoApp/index.html",
        {
            'title' : "Hello Django",
            'message' : "Hello Brydos!",
            'content': " on " + now.strftime("%A, %d %B, %Y at %X")
        }
    )

def about(request):
    return render(
        request,
        "HelloDjangoApp/about.html",
        {
            'title' : "About HelloDjangoApp",
            'content' : "Example app page for Django."
        }
    )
