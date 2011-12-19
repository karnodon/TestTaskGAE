from django.contrib.auth.views import login, logout
from django.conf.urls.defaults import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from TestTaskGAE.Test.views import chapters, task, end, add_answer, students, test_detail, tests, tests_to_pdf, test_chart, theory_reader, bio, feedback

#admin.autodiscover()
urlpatterns = patterns('',
    (r'^accounts/login/$', login),
    (r'^accounts/logout/$', logout),
    (r'^accounts/profile/$', chapters),
    (r'^chapter/$', chapters),
    (r'^chapter/([\d]*)/$', chapters),
    (r'^chapter/([\d]*)/final/$', chapters, {'final' : True}),
    (r'^chapter/([\d]*)/train/$', chapters, {'final' : False}),
    (r'^chapter/([\d]*)/task/0/$', end),
    (r'^chapter/[\d]*/task/([\d]*)/$', task),
    (r'^chapter/[\d]*/task/([\d]*)/answer/$', add_answer),
    (r'^theory/[\w]*.html$', theory_reader),
    (r'^statistics/students/$', students),
    (r'^statistics/tests/$', tests),
    (r'^statistics/tests/pdf/$', tests_to_pdf, {'chapterId' : 1}),
    (r'^statistics/test/([\d]*)/$', test_detail),
    (r'^statistics/chart/chapter/([\d]*)/student/([\d]*)/$', test_chart),
    (r'^bio/$', bio),
    (r'^feedback/$', feedback),
    # Example:
    # (r'^TestTask/', include('TestTask.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
#    (r'^admin/', include(admin.site.urls)),
    (r'^$', chapters),
)
#urlpatterns += patterns('',
#    url(r'^captcha/', include('captcha.urls')),
#)