from django.contrib import admin
from .models import Articles,Category

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title","slug","status","position")
    list_filter = ("title","status")
    # list_filter = (["status"])
    search_fields = ("title","slug")


admin.site.register(Category,CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title","slug","jpublished","status","category_to_str",)
    list_filter = ("published","status")
    search_fields = ("title","description")
    #  علامت منفی برای نزولی میباشد 
    status = ["-published","status"]

    def category_to_str(seslf,obj):
        return ",".join([category.title for category in obj.category.filter(status=True)])
    category_to_str.short_description = "دسته بندی"


admin.site.register(Articles,ArticleAdmin)
