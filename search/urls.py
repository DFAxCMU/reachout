from django.conf.urls import url

from search.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^search$', login_required(Search.as_view())),
]