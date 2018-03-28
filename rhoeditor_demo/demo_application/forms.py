from __future__ import absolute_import

from django import forms
from django_rholang_editor.fields import RholangTextFormField


class RhoEditorForm(forms.Form):
    content = RholangTextFormField()
