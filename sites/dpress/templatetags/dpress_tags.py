import re

from django.template import Library
from django.utils.safestring import mark_safe

from dpress.helper import tl_markdown
from dpress.models import Post

register = Library()

@register.filter
def md(_md):
    return tl_markdown(_md)

@register.inclusion_tag("dpress/tags/dummy.html")
def last_post(template='dpress/widgets/lastposts.html'):
    lastposts = Post.objects.filter(status=2).select_related(depth=1).order_by("-publish")
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
