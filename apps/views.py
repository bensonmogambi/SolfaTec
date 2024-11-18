from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def contact():
    return HttpResponse()


def blog(request):
    return render(request, 'Templates/blog.html')