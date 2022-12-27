from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from blog.models import Articles
# Create your views here.

@login_required
def home(request):
    template_name = "registration/home.html"
    return render(request, template_name=template_name)


class ArticleListView(ListView):
    queryset = Articles.objects.published_manager()
    template_name = "registration/home.html"

