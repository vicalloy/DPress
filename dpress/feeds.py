from django.contrib.syndication.views import Feed
from django.conf import settings
from django.core.urlresolvers import reverse

from .models import Post


class LatestDPressPostFeed(Feed):
    title = getattr(settings, 'DPRESS_TITLE', '')
    description = getattr(settings, 'DPRESS_DESCN', '')
    description_template = 'dpress/feeds/description.html'

    def items(self):
        return Post.objects.filter(status=2).order_by("-publish")[:10]

    def item_pubdate(self, item):
        return item.publish

    def link(self):
        return reverse('dpress_index')
