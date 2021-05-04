from django.urls import path, re_path
from .views import index, categories, show_post, archive, about, add_page, contact, login

urlpatterns = [
    path('', index, name = 'home'), # http://127.0.0.1:8000/
    path('about/', about, name = 'about'), # http://127.0.0.1:8000/about/
    path('cats/<slug:cat>/', categories, name = 'categories'), # http://127.0.0.1:8000/cats/1/
    path('addpage/', add_page, name = 'add_page'),
    path('contact/', contact, name = 'contact'),
    path('login/', login, name = 'login'),
    path('post/<int:post_id>/', show_post, name = 'post')
    # re_path(r'archive/(?P<year>[0-9]{4})/', archive), # http://127.0.0.1:8000/archive/2021/
]
