from django.urls import path, re_path
from .views import index, categories, archive

urlpatterns = [
    path('', index, name = 'home'), # http://127.0.0.1:8000/
    path('cats/<slug:cat>/', categories, name = 'categories'), # http://127.0.0.1:8000/cats/1/
    re_path(r'archive/(?P<year>[0-9]{4})/', archive), # http://127.0.0.1:8000/archive/2021/
]
