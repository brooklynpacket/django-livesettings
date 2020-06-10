from __future__ import unicode_literals
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.site_settings, {}, 'satchmo_site_settings'),
    url(r'^export/$', views.export_as_python, {}, 'settings_export'),
    url(r'^(?P<group>[^/]+)/$', views.group_settings),
]