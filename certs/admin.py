from django import forms
from django.contrib import admin

from .models import Certificate


class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        exclude = ['path']

class CertificateAdmin(admin.ModelAdmin):
    form = CertificateForm
    list_display = ('pk', 'type', 'subject', 'path')
    list_display_links = ('pk', 'subject', 'path')
    ordering = ('pk',)


admin.site.register(Certificate, CertificateAdmin)
