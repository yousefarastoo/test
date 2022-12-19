from django.shortcuts import render
from .models import Articles
# Create your views here.

def home(request):
    template = "blog/home.html"
    # context = {
    #     "articles":[
    #         {"name":"yousef","family":"arastoo","age":"33"},
    #         {"name":"satar","family":"nori","age":"23"},
    #         {"name":"reza","family":"rezaee","age":"25"},
    #         {"name":"sarah","family":"moradi","age":"19"},
    #     ]
    # }

    context = {
        "articles":Articles.objects.filter(status="p").order_by("-published")[:10]
    }
    return render(request, template_name=template,context = context)