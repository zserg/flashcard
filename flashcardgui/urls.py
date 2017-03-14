from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from flashcardgui import views


urlpatterns = [
    url('^$', views.home, name='home'),
    url('^profile/$', views.profile, name='profile'),

]

