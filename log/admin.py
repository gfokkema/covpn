from django.contrib import admin

from .models import LogEntry, LogEntryAttr


class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'type')
    ordering = ('pk',)


class LogEntryAttrAdmin(admin.ModelAdmin):
    list_display = ('logentry_pk', 'logentry_type', 'name', 'value')
    ordering = ('logentry', 'name', 'value')

    def logentry_pk(self, obj):
        return obj.logentry.pk

    def logentry_type(self, obj):
        return obj.logentry.type


admin.site.register(LogEntry, LogEntryAdmin)
admin.site.register(LogEntryAttr, LogEntryAttrAdmin)
