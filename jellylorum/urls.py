from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView
from django.views.generic.simple import redirect_to

from anime.models import Anime

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jellylorum.views.home', name='home'),
    # url(r'^jellylorum/', include('jellylorum.foo.urls')),
	url(r'^$', redirect_to, {'url': '/dia/'}),
	url(r'^dia/anime/$', ListView.as_view(model=Anime)),
	url(r'^dia/anime/(?P<slug>[\w-]+)/$', 'anime.views.details'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
)


