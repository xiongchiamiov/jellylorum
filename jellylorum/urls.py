from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jellylorum.views.home', name='home'),
    # url(r'^jellylorum/', include('jellylorum.foo.urls')),
	url(r'^$', redirect_to, {'url': '/dia/'}),
	url(r'^dia/anime/(?P<slug>[\w-]+)/$', 'anime.views.details'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
