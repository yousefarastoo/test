from django.contrib import admin
from .models import Articles

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title","slug","published","status")
    list_filter = ("published","status")
    search_fields = ("title","description")
    #  علامت منفی برای نزولی میباشد 
    status = ["-published","status"]


admin.site.register(Articles,ArticleAdmin)
# Register your models here.
