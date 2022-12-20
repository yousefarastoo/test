from django import template
from ..models import Category

register = template.Library()

@register.simple_tag
def title():
    return "وبلاگ جنگویی من"


@register.inclusion_tag("blog/partials/category_navbar.html")
def category_navbar():
    category = Category.objects.filter(status=True)
    return {
        "category" : category
    }
