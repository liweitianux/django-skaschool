# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.base import TemplateView

from archive.models import Archive, ArchiveCategory


class ArchiveView(TemplateView):
    """
    class-based view to show archives
    """
    template_name = 'archive/archive.html'

    def get_context_data(self, **kwargs):
        """
        add 'user' context
        """
        context = super(type(self), self).get_context_data(**kwargs)
        archive_categories = ArchiveCategory.objects.all()
        if Archive.objects.all():
            archive_empty = False
        else:
            archive_empty = True
        context['archive_categories'] = archive_categories
        context['archive_empty'] = archive_empty
        return context

