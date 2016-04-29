#what is the purpose of line 4, 5?
from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required

from user_accounts.views import *
# Create your views here.
urlpatterns = [
    url(r'^$', HomePage.as_view()),
    url(r'^login$', Login.as_view()),
    url(r'^logout$', Logout.as_view()),
    url(r'^register$', Register.as_view()),
    #url(r'^user$', login_required(UserPage.as_view()))
]