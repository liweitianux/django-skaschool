# -*- coding: utf-8 -*-

"""
App 'page' views
"""

from django.shortcuts import render
from django.views.generic.base import TemplateView

from notice.models import Notice


## IndexView for index page (django_skaschool/urls.py)
class IndexView(TemplateView):
    """
    class-based view for index page
    """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(type(self), self).get_context_data(**kwargs)
        # latest important notice (only display single one)
        important_notice_all = Notice.objects.filter(is_important=True).order_by('-pubtime')
        if important_notice_all:
            important_notice = important_notice_all[0]
        else:
            important_notice = None
        context['important_notice'] = important_notice
        return context


