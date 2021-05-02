from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

menu = ['Kategoriyalar' ,'Biz haqimizda', 'Bog\'lanish', "Ro'yhatdan o'tish"]

def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Asosiy sahifa'})

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'Biz haqimizda'})

def categories(request, cat):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Categories page</h1><p>Slug: {cat}</p>')

def archive(request, year):
    if int(year) > 2021:
        # raise Http404()
        return redirect('home', permanent = False) # True bo'lsa 301, False bo'lsa 302

    return HttpResponse(f'<h1>Arxiv malumotlar</h1><p>Year: {year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Bunday sahifa topilmadi</h1>')
