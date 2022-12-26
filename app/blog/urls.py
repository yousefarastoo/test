from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home , details,category_details,category,ArticleListView,author_list



app_name="blog"
urlpatterns = [
    path("home",ArticleListView.as_view(),name="home"),
    path("",home,name="home"),
    path("<int:page>",home,name="home"),
    path("articles/<slug:slug>",details,name="details"),
    path("category/",category,name="category"),
    path("category/<slug:slug>",category_details,name="category_details"),
    path("author/<slug:username>",author_list,name="author_list"),
    path("author/<slug:username>/<int:page>",author_list,name="author_list"),
]
