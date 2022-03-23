from django.urls import path, re_path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60)(WomenHome.as_view()), name = 'home'), # http://127.0.0.1:8000/
    path('about/', about, name = 'about'), # http://127.0.0.1:8000/about/
    path('cats/<slug:cat>/', categories, name = 'categories'), # http://127.0.0.1:8000/cats/1/
    path('addpage/', AddPage.as_view(), name = 'add_page'),
    path('contact/', ContactFormView.as_view(), name = 'contact'),
    path('register/', RegisterUser.as_view(), name = "register"),
    path('login/', LoginUser.as_view(), name = 'login'),
    path('logout/', logout_user, name = 'logout'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name = 'post'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name = 'category')
    # re_path(r'archive/(?P<year>[0-9]{4})/', archive), # http://127.0.0.1:8000/archive/2021/
]
