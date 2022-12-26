from django.shortcuts import render,get_object_or_404
from .models import Articles,Category
from django.core.paginator import Paginator
from django.views.generic import ListView,DetailView
from django.contrib.auth.models import User
import os
from config.settings import BASE_DIR


# Create your views here.

class ArticleListView(ListView):
    queryset = Articles.objects.filter(status="p")
    context_object_name="articles"
    template_name = "blog/myindex.html"
    paginate_by = 2
# article sectiom : 
def home(request,page=1):
    template = "blog/index.html"
    # categories = Category.objects.filter(slug="sport",status=True)
    # categories = categories.articles.all()
    # context = {
    #     "articles":[
    #         {"name":"yousef","family":"arastoo","age":"33"},
    #         {"name":"satar","family":"nori","age":"23"},
    #         {"name":"reza","family":"rezaee","age":"25"},
    #         {"name":"sarah","family":"moradi","age":"19"},
    #     ]
    # }
    # we can use list instead queryset for optimize : 
    # articles = list(Articles.objects.filter(status="p").order_by("-published")[:10])
    articles = Articles.objects.filter(status="p").order_by("-published")
    paginator = Paginator(articles, 2)
    context = {"articles":paginator.get_page(page),"categories":Category.objects.filter(status=True).order_by("position")}
    return render(request, template_name=template,context = context)

def details(reqest,slug):
    template_name = "blog/details.html"
    article = get_object_or_404(Articles,slug=slug,status="p")  
    context = {"article":article}
    return render(reqest, template_name,context)

# ---------------------------------------------------------------------------------------------


# category section 

def category(request):
    template_name="blog/category.html"
    categories= Category.objects.filter(status=True)
    context = {
        "categories":categories
    }
    return render(request,template_name=template_name,context=context)


def category_details(reqest,slug):
    template_name = "blog/category_datails.html"
    category = get_object_or_404(Category,slug=slug,status=True)    
    context = {"category":category}
    return render(reqest, template_name,context)

# ---------------------------------------------------------------------------------------------
def author_list(request,username,page=1):
    template_name="blog/author_list.html"
    author = get_object_or_404(User,username=username)
    paginator = Paginator(author.articles.published_manager(), 2)
    articles = paginator.get_page(page)
    context = {"author":author,"articles":articles}
    # print("============================")
    # for article in articles:
    #     print(article)
    # print("============================")
    return render(request, template_name=template_name,context=context)