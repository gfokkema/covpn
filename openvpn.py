#!/home/development/covpn/venv/bin/python
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'covpn.settings')
django.setup()

from log.models import create_log_entry
create_log_entry(os.environ.get('script_type'), **os.environ)
