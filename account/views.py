# -*- coding: utf-8 -*-

"""
views.py of app 'account'
"""

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, UpdateView
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect

from account.models import UserProfile
from account.forms import ResendEmailForm, UpdateProfileForm, UserFileFormSet


###### Class-based views ######
class ResendEmailView(FormView):
    """
    class-based view used to resend activation email
    if user provided different email, then update email to User instance
    """
    form_class = ResendEmailForm
    template_name = 'account/email_resend.html'
    success_url = reverse_lazy('email_resend_done')

    def form_valid(self, form):
        form.update_email()
        form.resend_email()
        return super(ResendEmailView, self).form_valid(form)


class ProfileView(TemplateView):
    """
    class view to show profile page
    """
    template_name = 'account/profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        user = self.request.user
        profile = user.userprofile_set.get(user=user)
        userfiles = user.userfile_set.all()
        context['user'] = user
        context['profile'] = profile
        context['userfiles'] = userfiles
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
        Returns the keyword arguments for instantiating the form
        and related formsets.
        modify this method to add 'email' data
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        # initialize form 'email' field
        user = self.request.user
        form.fields['email'].initial = user.email
        # formset and initialize with instances
        qset = user.userfile_set.all()
        formset = UserFileFormSet(instance=user, queryset=qset)
        return self.render_to_response(
                self.get_context_data(form=form, formset=formset))

    def post(self, request, *args, **kwargs):
        """
        handle POST requests, instantiating a form instance and
        related formset with passed POST data and then validate.
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ## formset
        # must pass 'instance' here, otherwise raise IndexError
        user = self.request.user
        formset = UserFileFormSet(self.request.POST, self.request.FILES,
                instance=user)
        if (form.is_valid() and formset.is_valid()):
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)

    def form_valid(self, form, formset):
        """
        modify 'form_valid' to update email field
        """
        form_data = form.cleaned_data
        # save object
        self.object = form.save()
        # update email and save
        user = self.request.user
        user.email = form_data.get('email', user.email)
        user.save()
        # formset
        formset.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, formset):
        """
        re-render the context data with the data-filled forms and errors
        """
        return self.render_to_response(
                self.get_context_data(form=form, formset=formset))


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


