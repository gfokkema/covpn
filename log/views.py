from django.shortcuts import get_object_or_404, render

from .models import LogEntry, LogEntryAttr


def index(request):
    context = {
        'log': LogEntry.objects.all()
    }
    return render(request, 'log/index.html', context)


def logentry(request, logentry_id):
    logentry = get_object_or_404(LogEntry, pk=logentry_id)
    context = {
        'attr': LogEntryAttr.objects.filter(logentry=logentry),
    }
    return render(request, 'log/logentry.html', context)
