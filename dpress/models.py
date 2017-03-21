# -*- coding: UTF-8 -*-
from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from taggit.managers import TaggableManager


class Category(models.Model):
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(_('slug'))

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categorys')
        ordering = ('title',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return ('dpress_category', None, {
            'category': self.slug
        })
    get_absolute_url = models.permalink(get_absolute_url)


class Post(models.Model):
    """Post model."""
    STATUS_CHOICES = (
        (1, _('Draft')),
        (2, _('Public')),
    )
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(_('slug'))
    author = models.ForeignKey(User, related_name="added_posts")
    body = models.TextField(_('body'))
    status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=1)
    publish = models.DateTimeField(_('publish'), default=datetime.now)
    created_at = models.DateTimeField(_('created at'), default=datetime.now)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)
    category = models.ForeignKey(
        Category, related_name="posts",
        blank=True, null=True, default=None, on_delete=models.SET_NULL)
    tags = TaggableManager(blank=True)

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        ordering = ('-publish',)
        get_latest_by = 'publish'

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return ('dpress_post', None, {
            'year': self.publish.year,
            'month': "%02d" % self.publish.month,
            'slug': self.slug
        })
    get_absolute_url = models.permalink(get_absolute_url)
