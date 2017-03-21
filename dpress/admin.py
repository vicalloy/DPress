# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib import admin
from pagedown.widgets import AdminPagedownWidget

from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'created_at', 'publish', )
    search_fields = ('title', 'body', )
    # raw_id_fields = ('author',)
    list_filter = ('category',)
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', )
    search_fields = ('title', 'slug', )


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
