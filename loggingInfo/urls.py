from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^logging_info_1/(?P<client_id>[a-zA-Z0-9_.-]+)', views.LoggingInfoOne, name='logging_info_1'),
    url(r'^logging_info_2/(?P<client_id>[a-zA-Z0-9_.-]+)', views.LoggingInfoTwo, name='logging_info_2'),
    url(r'^logging_info_3/(?P<client_id>[a-zA-Z0-9_.-]+)', views.LoggingInfoThree, name='logging_info_3'),
    url(r'^title_description/(?P<client_id>[a-zA-Z0-9_.-]+)$', views.TitleAndDescription, name = 'title_description'),
    url(r'^short_questions/(?P<client_id>[a-zA-Z0-9_.-]+)$', views.ShortQuestions, name='short_questions'),
    url(r'^log_all_info/(?P<client_id>[a-zA-Z0-9_.-]+)$', views.LogAllInfo, name='log_all_info'),
]