from django.conf.urls import url

from . import views
from loggingInfo.views import *

urlpatterns = [
# <<<<<<< HEAD
    # url(r'^logging_info_1/(?P<client_id>[a-zA-Z0-9_.-]+)', views.LoggingInfoOne, name='logging_info_1'),
    # url(r'^logging_info_2/(?P<client_id>[a-zA-Z0-9_.-]+)', views.LoggingInfoTwo, name='logging_info_2'),
    # url(r'^logging_info_3/(?P<client_id>[a-zA-Z0-9_.-]+)', views.LoggingInfoThree, name='logging_info_3'),
    # #url(r'^logging_info_1/$', views.LoggingInfoOne, name='logging_info_1'),
    # url(r'^title_description/(?P<client_id>[a-zA-Z0-9_.-]+)$', views.TitleAndDescription, name = 'title_description'),
    # url(r'^short_questions/(?P<client_id>[a-zA-Z0-9_.-]+)$', views.ShortQuestions, name='short_questions'),
    # url(r'^log_all_info/(?P<client_id>[a-zA-Z0-9_.-]+)$', views.LogAllInfo, name='log_all_info'),
    
    # url(r'^logging_info_2/(?P<client_id>[a-zA-Z0-9_.-]+)', views.LoggingInfoTwo, name='logging_info_2'),

    url(r'^logging_info_2/(?P<client_id>[a-zA-Z0-9_.-]+)', UpdateQuickInfo.as_view()),
#     # url(r'^logging_info_2/(?P<client_id>[a-zA-Z0-9_.-]+)', UpdateQuickInfo.as_view()),
# =======
#     url(r'^logging_info_1/(?P<client_id>[a-zA-Z0-9_.-]+)', views.LoggingInfoOne, name='logging_info_1'),
#     url(r'^logging_info_2/(?P<client_id>[a-zA-Z0-9_.-]+)', views.LoggingInfoTwo, name='logging_info_2'),
#     url(r'^logging_info_3/(?P<client_id>[a-zA-Z0-9_.-]+)', views.LoggingInfoThree, name='logging_info_3'),
#     url(r'^title_description/(?P<client_id>[a-zA-Z0-9_.-]+)$', views.TitleAndDescription, name = 'title_description'),
#     url(r'^short_questions/(?P<client_id>[a-zA-Z0-9_.-]+)$', views.ShortQuestions, name='short_questions'),
#     url(r'^log_all_info/(?P<client_id>[a-zA-Z0-9_.-]+)$', views.LogAllInfo, name='log_all_info'),
# >>>>>>> 881e2e177b08671a356471b8104293523d417ee5
]