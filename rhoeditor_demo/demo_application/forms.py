from __future__ import absolute_import

from django import forms
from rhoeditor.fields import RholangTextFormField


class RhoEditorForm(forms.Form):
    content = RholangTextFormField()
