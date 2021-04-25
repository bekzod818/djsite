from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Women app page</h1>')

def categories(request):
    return HttpResponse('<h1>Categories page</h1>')
