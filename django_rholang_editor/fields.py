from __future__ import absolute_import

from django import forms
from django.db import models
from .widgets import RhoEditorWidget


class RholangTextFields(models.TextField):
    def __init__(self, *args, **kwargs):
        super(RholangTextFields, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            "form_class": self._get_form_class()
        }
        defaults.update(kwargs)
        super(RholangTextFields, self).formfield(**defaults)

    @staticmethod
    def _get_form_class():
        return RholangTextFormField


class RholangTextFormField(forms.fields.CharField):
    def __init__(self, default_text="", height="400px", width="100%", js_variable="editor", *args, **kwargs):
        kwargs.update({"widget": RhoEditorWidget(default_text=default_text, height=height, width=width, js_variable=js_variable)})
        super(RholangTextFormField, self).__init__(*args, **kwargs)
