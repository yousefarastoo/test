from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home , details,category_details



app_name="blog"
urlpatterns = [
    path("",home,name="home"),
    path("articles/<slug:slug>",details,name="details"),
    path("category/<slug:slug>",category_details,name="category_details"),
]
