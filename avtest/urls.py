from django.conf.urls import url, include
from rest_framework import routers
import views

urlpatterns = [
    # Root
    url(r'^$', views.APIRoot.as_view(), name='api_root'),

    # Threat route
    url(r'^api/threat/ip/(?P<ip>(?:[0-9]{1,3}\.){3}[0-9]{1,3})$',
        views.IPDetailsView.as_view(),
        {'endpoint': 'api/threat/ip/'},
        name='threat_details'),

    # Traffic route
    url(r'^api/traffic$', views.Traffic.as_view(), name='traffic')
]
