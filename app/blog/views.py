from django.shortcuts import render,get_object_or_404
from .models import Articles

# Create your views here.

def home(request):
    template = "blog/index.html"
    # context = {
    #     "articles":[
    #         {"name":"yousef","family":"arastoo","age":"33"},
    #         {"name":"satar","family":"nori","age":"23"},
    #         {"name":"reza","family":"rezaee","age":"25"},
    #         {"name":"sarah","family":"moradi","age":"19"},
    #     ]
    # }
    article = Articles.objects.filter(status="p").order_by("-published")[:10] 
    context = {
        "articles":article
    }
    return render(request, template_name=template,context = context)

def details(req,slug):
    template_name = "blog/post.html"
    article = get_object_or_404(Articles,slug=slug,status="p")  
    context = {"article":article}
    return render(req, template_name,context)
