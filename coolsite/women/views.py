from django.shortcuts import render, redirect, get_object_or_404
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
    # cats = Category.objects.all()
    context = {
        'posts': posts,
        # 'cats': cats,
        'menu': menu,
        'title': 'Asosiy sahifa',
        'cat_selected': 0,
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

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id = cat_id)
    # cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        # 'cats': cats,
        'menu': menu,
        'title': 'Asosiy sahifa',
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context)

def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'women/post.html', context)

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
