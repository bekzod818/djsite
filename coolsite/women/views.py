from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *
from .forms import AddPostForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

menu = [
    {'title': 'Sayt haqida', 'url_name': 'about'},
    {'title': "Qo'shish", 'url_name': 'add_page'},
    {'title': 'Aloqa', 'url_name': 'contact'},
    {'title': 'Kirish', 'url_name': 'login'}
]


class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Bosh sahifa'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True)


# def index(request):
#     posts = Women.objects.all()
#     # cats = Category.objects.all()
#     context = {
#         'posts': posts,
#         # 'cats': cats,
#         'menu': menu,
#         'title': 'Asosiy sahifa',
#         'cat_selected': 0,
#     }
#     return render(request, 'women/index.html', context)

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'Biz haqimizda'})


# def add_page(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#
#     else:
#         form = AddPostForm()
#     return render(request, 'women/addpage.html', {'form': form, 'menu': menu, 'title': 'Maqola qo\'shish'})

class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Maqola qo\'shish'
        context['menu'] = menu
        return context


def contact(request):
    return render(request, 'women/contact.html', {'menu': menu})


def login(request):
    return render(request, 'women/login.html', {'menu': menu})


class WomenCategory(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Kategoriya - ' + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context


# def show_category(request, cat_id):
#     posts = Women.objects.filter(cat_id = cat_id)
#     # cats = Category.objects.all()
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         # 'cats': cats,
#         'menu': menu,
#         'title': 'Asosiy sahifa',
#         'cat_selected': cat_id,
#     }
#     return render(request, 'women/index.html', context)

class ShowPost(DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post']
        context['menu'] = menu
        return context


# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#     return render(request, 'women/post.html', context)

def categories(request, cat):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Categories page</h1><p>Slug: {cat}</p>')


def archive(request, year):
    if int(year) > 2021:
        # raise Http404()
        return redirect('home', permanent=False)  # True bo'lsa 301, False bo'lsa 302

    return HttpResponse(f'<h1>Arxiv malumotlar</h1><p>Year: {year}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Bunday sahifa topilmadi</h1>')
