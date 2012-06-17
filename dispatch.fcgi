#!/usr/bin/python
from flup.server.fcgi import WSGIServer
from django.core.handlers.wsgi import WSGIHandler
import sys, os

sys.path += [os.path.join(os.path.dirname(__file__), '..')]
os.environ['DJANGO_SETTINGS_MODULE'] = 'kusskr.settings'
WSGIServer(WSGIHandler()).run()

