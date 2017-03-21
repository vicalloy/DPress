from django.conf.urls import url

from . import views
from .feeds import LatestDPressPostFeed


urlpatterns = [
    url(r'^$', views.index, name='dpress_index'),
    url(r'^a/(?P<year>\d{4})/(?P<month>\d{1,2})/$', views.index, name='dpress_month_archive'),
    url(r'^c/(?P<category>[-\w]+)/$', views.index, name='dpress_category'),
    url(r'^tags/(?P<tag>[-\w]+)/$', views.index, name='dpress_tag'),
    url(r'^post/(?P<year>\d{4})/(?P<month>\d{2})/(?P<slug>[-\w]+)/$',
        views.post, name='dpress_post'),
    url(r'^latest/feed/$', LatestDPressPostFeed(), name="dpress_feeds"),
]
