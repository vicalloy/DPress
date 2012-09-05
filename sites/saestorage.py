# -*- coding: utf-8 -*-
import os, time, random 
from django.core.files.base import File
from django.core.files.storage import Storage
from django.conf import settings 
from django.core.files import File
import sae.storage
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

class SaeStorage(Storage):
     
    def __init__(self, location="base"
            #accesskey=settings.ACCESS_KEY, 
            #secretkey=settings.SECRET_KEY, 
            #prefix=settings.APP_NAME
            #media_root=settings.MEDIA_ROOT,
            #media_url=settings.MEDIA_URL,
            ): 
        #self.accesskey = accesskey
        #self.secretkey = secretkey
        #self.prefix = prefix
        #self.media_root = media_root
        #self.media_url = media_url

        #self.client = sae.storage.Client(accesskey, secretkey, prefix)
        self.prefix = location
        self.client = sae.storage.Client()

    def _put_file(self, name, content):
        ob = sae.storage.Object(content)
        self.client.put(self.prefix, name, ob)

    def _read(self, name):
        memory_file = StringIO()
        try:
            o = self.client.get(self.prefix, name)
            memory_file.write(o.data)
        except sae.storage.ObjectNotExistsError, e:
            pass
        return memory_file

    def _open(self, name, mode="rb"):
        return SaeStorageFile(name, self, mode=mode)

    def _save(self, name, content): 
        content.open()
        if hasattr(content, 'chunks'):
            content_str = ''.join(chunk for chunk in content.chunks())
        else:
            content_str = content.read()
        #for fake tempfile
        if not content_str and hasattr(content, "file"):
            try:
                content_str = content.file.getvalue()
            except:
                pass
        self._put_file(name, content_str)
        content.close()
        return name

    def delete(self, name):
        self.client.delete(self.prefix, name)

    def exists(self, name):
        try:
            o = self.client.stat(self.prefix, name)
        #except sae.storage.ObjectNotExistsError, e:
        except:
            return False
        return True

    def listdir(self, domain):
        #sae no folder
        files = self.client.list(self.prefix)
        return ((), tuple(f['name'] for f in files))
        
    def size(self, name):
        try:
            stat = self.client.stat(self.prefix, name)
        except sae.storage.ObjectNotExistsError, e:
            return 0
        return stat.length

    def url(self, name):
        return self.client.url(self.prefix, name)
        
    def isdir(self, name):
        return False if name else True

    def isfile(self, name):
        return self.exists(name) if name else False
        
    def modified_time(self, name):
        from datetime import datetime
        return datetime.now()
        
class SaeStorageFile(File):
    """docstring for SaeStorageFile"""
    def __init__(self, name, storage, mode):
        self._name = name
        self._storage = storage
        self._mode = mode
        self._is_dirty = False
        self.file = StringIO()
        self._is_read = False

    @property
    def size(self):
        if not hasattr(self, '_size'):
            self._size = self._storage.size(self._name)
        return self._size

    def read(self, num_bytes=None):
        if not self._is_read:
            self.file = self._storage._read(self._name)
            self.file = StringIO(self.file.getvalue())
            self._is_read = True
        if num_bytes:
            return self.file.read(num_bytes)
        else:
            return self.file.read()
            
    def write(self, content):
        if 'w' not in self._mode:
            raise AttributeError("File was opened for read-only access.")
        self.file = StringIO(content)
        self._is_dirty = True
        self._is_read = True

    def close(self):
        if self._is_dirty:
            self._storage._put_file(self._name, self.file.getvalue())
        self.file.close()
