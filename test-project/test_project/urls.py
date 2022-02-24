from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('settings/', include('livesettings.urls')),
    path('admin/', include(admin.site.urls)),
    path('accounts/login/', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}),
    path('', 'localsite.views.index')
]
