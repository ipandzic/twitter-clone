from django.conf.urls import url
from django.views.generic.base import RedirectView

from .views import (PublicTweetListView, TweetCreateView, TweetDeleteView,
                    TweetDetailView, TweetListView, TweetUpdateView)

urlpatterns = [
    url(r'^$', RedirectView.as_view(url="/")),
    url(r'^list/$', TweetListView.as_view(), name='list'),
    url(r'^public/$', PublicTweetListView.as_view(), name='public'),
    url(r'^create/$', TweetCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'),
]
