from __future__ import absolute_import

from django import forms
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from js_asset import JS


class RhoEditorWidget(forms.Textarea):
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

    def render(self, name, value, attrs=None, renderer=None):
        return mark_safe(render_to_string(
            "rhoeditor/widget.html",
            {
                "default_text": self._default_text,
                "height": self._height,
                "width": self._width,
                "variable": self._js_variable,
                "widget_name": name

            }
        ))
