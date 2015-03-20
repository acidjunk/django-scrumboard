from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = patterns('',
    url(r'^$',include('scrumtools.apps.staticpage.urls', namespace='page')),
    url(r'^wishlist/', include('scrumtools.apps.wishlist.urls', namespace='wishlist')),
    url(r'^scrumboard/', include('scrumtools.apps.scrumboard.urls', namespace='scrumboard')),
    url(r'^page/', include('scrumtools.apps.staticpage.urls', namespace='page')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('scrumtools.api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/token/', obtain_auth_token, name='api-token'),
)