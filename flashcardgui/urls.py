from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from flashcardgui import views


urlpatterns = [
    url('^$', views.home, name='home'),
    url('^about/$', views.about, name='about'),
    url('^profile/$', views.profile, name='flashcardgui.views.profile'),
    url('^add/$', views.add, name='add-card'),

]

