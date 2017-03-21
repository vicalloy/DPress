from django.template import Library

from dpress.helper import tl_markdown
from dpress.models import Post
from dpress.models import Category

register = Library()


@register.filter
def md(_md):
    return tl_markdown(_md)


@register.inclusion_tag("dpress/tags/dummy.html")
def last_post(template='dpress/widgets/lastposts.html'):
    lastposts = Post.objects.filter(status=2).select_related().order_by("-publish")
    return {
        "template": template,
        'lastposts': lastposts[:5]
    }


@register.inclusion_tag("dpress/tags/dummy.html")
def month_links(template="dpress/widgets/monthlinks.html"):
    return {
        "template": template,
        'dates': Post.objects.filter(status=2).dates('publish', 'month')[:12],
    }


@register.inclusion_tag("dpress/tags/dummy.html")
def categorys(template="dpress/widgets/categorys.html"):
    return {
        "template": template,
        'categorys': Category.objects.order_by("title"),
    }
