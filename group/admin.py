from django.contrib import admin

from .models import Config, Route


class ConfigAdmin(admin.ModelAdmin):
    list_display = ('group', 'option', 'value')
    ordering = ('group', 'option')


class RouteAdmin(admin.ModelAdmin):
    list_display = ('group', 'ip', 'mask', 'gateway', 'metric')
    ordering = ('group', 'ip')


admin.site.register(Config, ConfigAdmin)
admin.site.register(Route, RouteAdmin)
