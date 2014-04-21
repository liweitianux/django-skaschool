# -*- coding: utf-8 -*-

"""
views.py of app 'account'
"""

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

from account.models import UserProfile
from account.forms import UpdateProfileForm


###### Class-based views ######
class ProfileView(TemplateView):
    """
    class view to show profile page
    """
    template_name = 'account/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        user = self.request.user
        profile = user.userprofile_set.get(user=user)
        context['user'] = user
        context['profile'] = profile
        return context


class UpdateProfileView(UpdateView):
    form_class = UpdateProfileForm
    model = UserProfile
    template_name = 'account/profile_update.html'
    success_url = reverse_lazy('profile_update_done')

    # get profile object
    def get_object(self, queryset=None):
        user = self.request.user
        profile = user.userprofile_set.get(user=user)
        return profile

    def get(self, request, *args, **kwargs):
        """
        Returns the keyword arguments for instantiating the form.
        modify this method to add 'email' data
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        # initialize form 'email' field
        user = self.request.user
        form.fields['email'].initial = user.email
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        """
        modify 'form_valid' to update email field
        """
        form_data = form.cleaned_data
        # update email and save
        user = self.request.user
        user.email = form_data.get('email', user.email)
        user.save()
        return super(UpdateProfileView, self).form_valid(form)


class ListApprovedView(ListView):
    """
    class-based view to show list of approved users
    """
    queryset = UserProfile.objects.filter(is_approved='Y')
    template_name = 'account/list_approved.html'
    # allow queryset/model returns no object, otherwise 404error raised
    allow_empty = True

    def get_context_data(self, **kwargs):
        """
        add 'user' context
        """
        context = super(ListApprovedView, self).get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user
        return context


