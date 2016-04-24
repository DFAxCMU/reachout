from django.conf.urls import url

from search.views import *

urlpatterns = [
    url(r'^$', Search.as_view()),
]