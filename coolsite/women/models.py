from django.db import models
from django.urls import reverse

class Women(models.Model):
    title = models.CharField(max_length = 255, verbose_name = 'Sarlavha')
    slug = models.SlugField(max_length = 255, unique = True, db_index = True, verbose_name = 'URL')
    content = models.TextField(blank = True, verbose_name = 'Matn')
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/', verbose_name = 'Rasm')
    time_create = models.DateTimeField(auto_now_add = True, verbose_name = 'Yaratilgan sana')
    time_update = models.DateTimeField(auto_now = True, verbose_name = "O'zgartirilgan sana")
    is_published = models.BooleanField(default = True, verbose_name = 'Publikatsiya')
    cat = models.ForeignKey('Category', on_delete = models.PROTECT, verbose_name = 'Kategoriya')

    class Meta:
        verbose_name = 'Mashhur ayol'
        verbose_name_plural = 'Mashhur ayollar'
        ordering = ['-time_update']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs = {'post_slug': self.slug})

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name = 'Kategoriya')
    slug = models.SlugField(max_length = 255, unique = True, db_index = True, verbose_name = 'URL')

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'
        ordering = ['id']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs = {'cat_slug': self.slug})
