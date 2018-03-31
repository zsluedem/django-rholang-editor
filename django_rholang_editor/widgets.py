from __future__ import absolute_import

from django import forms
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from js_asset import JS


class RhoEditorWidget(forms.Widget):
    template_name = "rhoeditor/widget.html"
    class Media:
        js = (
            JS("rhoeditor/rhoeditor/ace.js", {}),
            JS("rhoeditor/rhoeditor/ext-language_tools.js", {})
        )

    def __init__(self, default_text="", height="400px", width="100%", js_variable="editor", *args, **kwargs):
        self._default_text = default_text
        self._height = height
        self._width = width
        self._js_variable = js_variable
        super(RhoEditorWidget, self).__init__(*args, **kwargs)

    def get_context(self, name, value, attrs):
        context = super(RhoEditorWidget, self).get_context(name, value, attrs)
        context['widget']['default_text'] = self._default_text
        context['widget']['height'] = self._height
        context['widget']['width'] = self._width
        context['widget']['variable'] = self._js_variable
        return context


    def render(self, name, value, attrs=None, renderer=None):
        context = self.get_context(name, value, attrs)
        return mark_safe(render_to_string(
            self.template_name,
            context
        ))
