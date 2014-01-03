import os
import sys

normpath = lambda *args: os.path.normpath(os.path.abspath(os.path.join(*args)))

PROJECT_ROOT = normpath(__file__, "..")

if os.path.exists(normpath(PROJECT_ROOT, "project", "settings.py")):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.root_settings")

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()