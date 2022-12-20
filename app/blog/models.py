from django.db import models
from django.utils import timezone
from .extensions.jalali import jalali_convertor

class Articles(models.Model):
    draft = "d"
    publish = "p"
    STATUS_CHOICES = [
        (draft,"پیش نویس"),
        (publish,"منتشر شده")
    ]
    title = models.CharField(max_length=250,verbose_name="عنوان مقاله")
    slug = models.SlugField(max_length=250,verbose_name="اسلاگ")
    description = models.TextField(verbose_name="مقاله")
    published = models.DateTimeField(default=timezone.now,verbose_name="تاریخ انتشار")
    thumbnail = models.ImageField(upload_to="images",verbose_name="عکس")
    created = models.DateTimeField(auto_now_add=True,verbose_name="تاریخ ایجاد مقاله")
    updated = models.DateTimeField(auto_now=True,verbose_name="تاریخ آپدیت")
    status = models.CharField(max_length=1,choices=STATUS_CHOICES,default=draft,verbose_name="وضعیت")

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
    
    def jpublished(self):
        return jalali_convertor(self.published)
    jpublished.short_description = "زمان انتشار"

    def __str__(self):
        return self.title

