from django.conf.urls import url

from profiles.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^client/(?P<client_id>[a-zA-Z0-9_.-]+)$', login_required(ClientProfile.as_view())),
    url(r'^timeline/(?P<client_id>[a-zA-Z0-9_.-]+)$', login_required(Timeline.as_view())),
    url(r'^new_client$', NewClientProfile.as_view()),
    #url(r'^$', views.index, name='profiles'),
]