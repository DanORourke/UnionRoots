from django.shortcuts import render, get_object_or_404
from . import models
from django.views.generic import TemplateView, ListView


class HomePageView(TemplateView):
    template_name = 'home/home.html'


class SimpleMarkdownView(TemplateView):
    template_name = 'home/simple_markdown.html'

    def get_context_data(self, **kwargs):
        context = super(SimpleMarkdownView, self).get_context_data(**kwargs)
        context['object'] = get_object_or_404(models.SimpleMarkdown, name=self.kwargs['slug'])
        return context

