# DPress

DPress is a simple blog powerd by Django.

## Features

+ [Markdown](http://daringfireball.net/projects/markdown/)
+ use [EpicEditor](http://epiceditor.com/) as Markdown Editor.
+ [DISQUS](http://disqus.com/)
+ Code Highlight. Syntax: [Fenced Code Blocks](http://packages.python.org/Markdown/extensions/fenced_code_blocks.html)
+ use [Django FileBrowser](https://github.com/sehmaschine/django-filebrowser) to upload files.
+ use [flatpages](https://docs.djangoproject.com/en/dev/ref/contrib/flatpages/) to manage custom page.
+ GOOGLE ANALYTICS
+ RSS
+ Tags

## run on Django dev server

+ Clone DPress repository from git://github.com/vicalloy/DPress.git
+ use scripts/create_env.py to create DPress environment(create python virtualenv, install requirements libs)
+ use scriptsenv.bat(source env.rc) to start DPress environment.
+ %mg%($mg in linux) is a shortcut for "python manage.py "
+ %mg% syncdb
+ %mg% runserver
+ DPress Admin http://127.0.0.1:8000/admin/
+ DPress http://127.0.0.1:8000/