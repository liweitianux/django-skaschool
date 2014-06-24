# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.base import TemplateView

from schedule.models import Event, EventAttachment

import re
import datetime


class ScheduleView(TemplateView):
    """
    class-based view to show events with their attachments
    generate the schedule page
    """
    template_name = 'schedule/schedule.html'

    def get_context_data(self, **kwargs):
        context = super(type(self), self).get_context_data(**kwargs)
        event_all_qs = Event.objects.all().order_by('date')
        if event_all_qs:
            event_empty = False
            # get all the dates 
            day_all = ['%s'%e.date.isoformat() for e in event_all_qs]
            # deduplicate while preserver order
            tmplist = []
            for e in day_all:
                if e not in tmplist:
                    tmplist.append(e)
            day_all[:] = tmplist
            # make a dict to group events by date
            event_dict = {}
            for d in day_all:
                day = datetime.date(*map(int, re.split('[^\d]', d)))
                event_day = event_all_qs.filter(date=day).order_by('time_start')
                event_dict[d] = event_day
            # get time of last update
            event_last_updated = event_all_qs.order_by('-updated_at')[0]
            updated_at = event_last_updated.updated_at.isoformat()
        else:
            event_empty = True
            event_dict = {}
            day_all = []
            updated_at = 'N/A'
        #
        context['event_empty'] = event_empty
        context['event_dict'] = event_dict
        context['day_all'] = day_all
        context['updated_at'] = updated_at
        return context

