from django.conf.urls import include, url
from gtfs.views import StopList, StopDetail, ClosestStopList

urlpatterns = [
    url(r'^stops/$', StopList.as_view()),
    url(r'^stops/(?P<pk>[0-9]+)/$', StopDetail.as_view()),
    url(r'^stops/closest/(?P<coords>[0-9.]+,[0-9.]+)/$', ClosestStopList.as_view()),
]
