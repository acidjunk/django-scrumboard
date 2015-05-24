from django.conf.urls import patterns, url

from scrumtools.apps.wishlist import views

urlpatterns = patterns('',
    # ex: /wishlist
    url(r'^$', views.WishList.as_view(), name='wish-list'),
    url(r'^detail/(?P<pk>\d+)$', views.WishDetail.as_view(), name='wish-detail'),
    url(r'^new$', views.WishCreate.as_view(), name='wish-new'),
    url(r'^edit/(?P<pk>\d+)$', views.WishUpdate.as_view(), name='wish-edit'),
    url(r'^delete/(?P<pk>\d+)$', views.WishDelete.as_view(), name='wish-delete'),
)
