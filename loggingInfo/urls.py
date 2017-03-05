from django.conf.urls import url

from . import views
from loggingInfo.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^log_interaction/(?P<client_id>[a-zA-Z0-9_.-]+)', login_required(LogInteraction.as_view())),
]