from django.shortcuts import get_object_or_404, render

from .models import Group, Config, Route


def index(request, group_name):
    group = get_object_or_404(Group, name=group_name)
    context = {
        'config': Config.objects.filter(group=group),
        'routes': Route.objects.filter(group=group),
    }
    return render(request, 'group/index.html', context)
