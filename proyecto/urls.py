

from django.conf.urls import *
from django.contrib import admin

admin.autodiscover()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^prueba/$','blog.views.archive'),
    url(r'^$','blog.views.archive'),
]