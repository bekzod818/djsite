from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

def index(request):
    return HttpResponse('<h1>Women app page</h1>')

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
