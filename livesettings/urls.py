from __future__ import unicode_literals
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.site_settings, {}, 'satchmo_site_settings'),
    path('export/', views.export_as_python, {}, 'settings_export'),
    re_path('^(?P<group>[^/]+)/$', views.group_settings),
]
