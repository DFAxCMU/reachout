from django.conf.urls import url

from search.views import *

urlpatterns = [
    url(r'^search$', Search.as_view()),
]