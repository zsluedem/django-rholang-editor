# coding=utf8

from django.urls import reverse
from django.views import generic

from .forms import RhoEditorForm


class RhoEditorFormView(generic.FormView):
    form_class = RhoEditorForm
    template_name = "form.html"

    def get_success_url(self):
        return reverse("rhoeditor-form")
