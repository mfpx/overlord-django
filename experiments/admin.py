from django.contrib import admin

from .models import Experiment, Description

admin.site.register(Experiment)
admin.site.register(Description)
