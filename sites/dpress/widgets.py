from django import forms
from django.conf import settings
from django.contrib.admin import widgets as admin_widgets
from django.core.urlresolvers import reverse
from django.forms.widgets import flatatt
try:
    from django.utils.encoding import smart_unicode
except ImportError:
    from django.forms.util import smart_unicode
from django.utils.html import escape
from django.utils import simplejson
from django.utils.datastructures import SortedDict
from django.utils.safestring import mark_safe
from django.utils.translation import get_language, ugettext as _

class EpicEditorWidget(forms.Textarea):

    def __init__(self, *args, **kwargs):
        super(EpicEditorWidget, self).__init__(*args, **kwargs)

    def render(self, name, value, attrs=None):
        cfg = {"container": "epic_body_id", "autoSave": False, 'clientSideStorage': False}
        cfg['basePath'] = getattr(settings, 'EPIC_BASEPATH', '/static/dpress/epiceditor')
        cfg_f = {'name': 'body'}
        cfg_f['defaultContent'] = value
        cfg['file'] = cfg_f
        cfg_json = simplejson.dumps(cfg)
        hide_field = super(EpicEditorWidget, self).render(name, value, attrs)
        html = u"""
        <div id="epic_body_id" style="height: 300px"></div>
        <div style="display: none">%s</div>
        <script type="text/javascript">
        (function($){
            $(function(){
                var bdEditor = new EpicEditor(%s).load(); 
                //bdEditor.getElement('editor').body.innerHTML
                $('#post_form').submit(function(){$('#id_body').val(bdEditor.exportFile())});
            });
        }(grp.jQuery));
        </script>
        """ % (hide_field, simplejson.dumps(cfg), )
        return mark_safe(html)

    def _media(self):
        epic_js = getattr(settings, 'EPIC_JS', 'dpress/epiceditor/js/epiceditor.min.js')
        return forms.Media(js=[epic_js])
    media = property(_media)
