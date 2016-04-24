from django.conf.urls import url

from profiles.views import *

urlpatterns = [
    url(r'^client/(?P<client_id>[a-zA-Z0-9_.-]+)$', ClientProfile.as_view()),
    url(r'^timeline/(?P<client_id>[a-zA-Z0-9_.-]+)$', Timeline.as_view()),
    url(r'^new_client$', NewClientProfile.as_view()),
    #url(r'^$', views.index, name='profiles'),
]