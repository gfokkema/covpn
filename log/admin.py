from django.contrib import admin

from .models import LogEntry, LogEntryAttr

admin.site.register([LogEntry, LogEntryAttr])
