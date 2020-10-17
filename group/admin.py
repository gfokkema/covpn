from django.contrib import admin

from .models import Group, Config, Route

admin.site.register([Group, Config, Route])
