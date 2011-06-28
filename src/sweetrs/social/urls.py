__author__ = 'kidzik'
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^friends/$', 'sweetrs.social.views.social_friends', {} ,'social_friends'),
)
  