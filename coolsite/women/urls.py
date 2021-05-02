from django.urls import path, re_path
from .views import index, categories, archive, about

urlpatterns = [
    path('', index, name = 'home'), # http://127.0.0.1:8000/
    path('about/', about, name = 'about'), # http://127.0.0.1:8000/about/
    path('cats/<slug:cat>/', categories, name = 'categories'), # http://127.0.0.1:8000/cats/1/
    # re_path(r'archive/(?P<year>[0-9]{4})/', archive), # http://127.0.0.1:8000/archive/2021/
]
