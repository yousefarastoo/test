from django.shortcuts import render,get_object_or_404
from .models import Articles,Category

# Create your views here.


# article sectiom : 
def home(request):
    template = "blog/index.html"

    categories = Category.objects.filter(slug="sport",status=True)
    # categories = categories.articles.all()
    print("=======================")
    for cat in list(categories):
        print(cat.articles.all())
    print("=======================")
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
    articles = Articles.objects.filter(status="p").order_by("-published")[:10]
    context = {"articles":articles,"categories":Category.objects.filter(status=True).order_by("position")}
    return render(request, template_name=template,context = context)

def details(reqest,slug):
    template_name = "blog/post.html"
    article = get_object_or_404(Articles,slug=slug,status="p")  
    context = {"article":article}
    return render(reqest, template_name,context)

# ---------------------------------------------------------------------------------------------


# category section 

def category_details(reqest,slug):
    template_name = "blog/category_datails.html"
    category = get_object_or_404(Category,slug=slug,status=True)    
    context = {"category":category}
    return render(reqest, template_name,context)

# ---------------------------------------------------------------------------------------------
