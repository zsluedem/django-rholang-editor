# coding=utf8

from django.views import generic
from .forms import RhoEditorForm
from django.urls import reverse


class RhoEditorFormView(generic.FormView):
    form_class = RhoEditorForm
    template_name = "form.html"

    def get_success_url(self):
        return reverse("rhoeditor-form")