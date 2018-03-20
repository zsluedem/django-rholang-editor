from __future__ import absolute_import

from django import forms
from django.db import models
from .widgets import RhoEditorWidget


class RholangTextFiels(models.TextField):
    def __init__(self, *args, **kwargs):
        super(RholangTextFiels, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            "form_class":self._get_form_class()
        }
        defaults.update(kwargs)
        super(RholangTextFiels, self).formfield(**defaults)
        
    @staticmethod
    def _get_form_class():
        return RholangTextFormField

class RholangTextFormField(forms.fields.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.update({"widget":RhoEditorWidget()})
        super(RholangTextFormField, self).__init__(*args, **kwargs)
