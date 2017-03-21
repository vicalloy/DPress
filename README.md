# DPress

DPress is a simple blog powered by Django.

## Features

+ [Markdown](http://daringfireball.net/projects/markdown/)
+ [DISQUS](http://disqus.com/)
+ Code Highlight. Syntax: [Fenced Code Blocks](http://packages.python.org/Markdown/extensions/fenced_code_blocks.html)
+ use [Django FileBrowser](https://github.com/sehmaschine/django-filebrowser) to upload files.
+ use [flatpages](https://docs.djangoproject.com/en/dev/ref/contrib/flatpages/) to manage custom page.
+ GOOGLE ANALYTICS
+ RSS
+ Tags

## run on Django dev server

+ Clone DPress repository from git://github.com/vicalloy/DPress.git
+ install virtualenv: pip install virtualenv 
+ use scripts env.rc(`source env.rc`) to create and start DPress environment.
+ $mg is a shortcut for "python manage.py "
+ $mg migrate
+ $mg runserver
+ DPress Admin http://127.0.0.1:8000/admin/
+ DPress http://127.0.0.1:8000/

## config

+ copy dpress_site/settings/local.sample to dpress_site/settings/local.py and config it.
