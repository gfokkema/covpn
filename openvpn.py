#!/home/development/covpn/venv/bin/python
import django
import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'covpn.settings')
django.setup()

from django.contrib.auth.models import User
from group.models import Config, Route
from log.models import create_log_entry


class Dispatcher:
    def __init__(self, *args, **kwargs):
        type = kwargs.get('script_type')
        if not type:
            raise Exception("`script_type` empty")

        create_log_entry(type, **kwargs)
        fn = getattr(self, type.replace('-', '_'))
        if not fn:
            raise Exception("`script_type` not defined: {0.script_type}".format(kwargs))

        fn(*args, **kwargs)

    def client_connect(self, *args, **kwargs):
        (_, ccd) = args
        groups = User.objects.get(username=kwargs.get('common_name')).groups.all()
        rules = [
            *Config.objects.filter(group__in=groups),
            *Route.objects.filter(group__in=groups),
        ]
        with open(ccd, 'w') as f:
            for rule in rules:
                f.write('push "{}"\n'.format(rule))

    def client_disconnect(self, *args, **kwargs):
        pass


if __name__ == '__main__':
    Dispatcher(*sys.argv, **os.environ)
