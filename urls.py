from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^bookmarkThis/', include('bookmarkThis.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
	(r'^accounts/login/$', 'django.contrib.auth.views.login'),
	(r'^accounts/register/$', 'bookmarkThis.users.views.register'),
	(r'^accounts/user-profile/$', 'bookmarkThis.users.views.userProfile'),
	(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
	(r'^bookmark/(?P<bookmark_id>\d+)/vote/(?P<verdictInput>\d+)/','bookmarkThis.bookmarkEntry.views.bookmarkDetail'),
	(r'^bookmark/(?P<bookmark_id>\d+)/','bookmarkThis.bookmarkEntry.views.bookmarkDetail'),
	(r'^create-bookmark/','bookmarkThis.bookmarkEntry.views.createBookmark'),
	(r'^$', 'bookmarkThis.bookmarkEntry.views.default'),
)
