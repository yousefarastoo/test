from django.contrib import admin
from .models import Articles

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title","slug","publish","status")


admin.site.register(Articles,ArticleAdmin)
# Register your models here.
