import os,sys
os.environ['DJANGO_SETTINGS_MODULE'] = 'TestTaskGAE.settings'

# Force Django to reload its settings.
from django.conf import settings
settings._target = None

import django.core.handlers.wsgi
import django.core.signals
import django.db
import django.dispatch

# Log errors.
#import logging
#def log_exception(*args, **kwds):
#    logging.exception('Exception in request:')
#
#django.dispatch.Signal.connect(
#    django.core.signals.got_request_exception, log_exception)

# Unregister the rollback event handler.
django.dispatch.Signal.disconnect(
    django.core.signals.got_request_exception,
    django.db._rollback_on_exception)

app = django.core.handlers.wsgi.WSGIHandler()
#import webapp2

#class MainPage(webapp2.RequestHandler):
#    def get(self):
#        self.response.headers['Content-Type'] = 'text/plain'
 #       self.response.out.write('Hello, webapp World!')

#app = webapp2.WSGIApplication([('/', MainPage)], debug=True)