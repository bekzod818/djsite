from django.urls import path
from .views import index, categories

urlpatterns = [
    path('', index, name = 'index'),
    path('cats/', categories, name = 'categories')
]
