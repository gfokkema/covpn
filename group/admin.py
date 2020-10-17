from django.contrib import admin

from .models import Config, Route


class ConfigAdmin(admin.ModelAdmin):
    list_display = ('group', 'option', 'value')
    list_display_links = ('group',)


class RouteAdmin(admin.ModelAdmin):
    list_display = ('group', 'ip', 'mask', 'gateway', 'metric')
    list_display_links = ('group',)

admin.site.register(Config, ConfigAdmin)
admin.site.register(Route, RouteAdmin)
