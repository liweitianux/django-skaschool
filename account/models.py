# -*- coding: utf-8 -*-
#
# app 'account' models
# registration, login, etc.
#

from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)

