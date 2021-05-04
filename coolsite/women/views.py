from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

menu = [
    {'title': 'Sayt haqida', 'url_name': 'about'},
    {'title': "Qo'shish", 'url_name': 'add_page'},
    {'title': 'Aloqa', 'url_name': 'contact'},
    {'title': 'Kirish', 'url_name': 'login'}
]

def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Asosiy sahifa'
    }
    return render(request, 'women/index.html', context)

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'Biz haqimizda'})

def add_page(request):
    return render(request, 'women/add.html', {'menu': menu})

def contact(request):
    return render(request, 'women/contact.html', {'menu': menu})

def login(request):
    return render(request, 'women/login.html', {'menu': menu})

def show_post(request, post_id):
    return HttpResponse(f"Post id = {post_id}")

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
