# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.list import ListView

from notice.models import Notice


class ListNoticeView(ListView):
    """
    class-based view to show list of notice
    """
    queryset = Notice.objects.all()     # default order by '-pubtime'
    template_name = 'notice/list_notice.html'
    # allow queryset/model returns no object, otherwise 404error raised
    allow_empty = True

    def get_context_data(self, **kwargs):
        """
        add 'user' context
        """
        context = super(ListNoticeView, self).get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user
        return context

