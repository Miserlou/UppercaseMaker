from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^(?P<input>[^/]+)$', 'UppercaseMaker.upper.views.home'),
    url(r'^admin/', include(admin.site.urls)),
)
