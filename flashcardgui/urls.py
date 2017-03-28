from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from flashcardgui import views


urlpatterns = [
    url('^$', views.home, name='home'),
    url('^about/$', views.about, name='about'),
    url('^profile/$', views.profile, name='flashcardgui.views.profile'),
    url('^add/$', views.add, name='add-card'),
    url('^study/(?P<deck_id>[0-9]+)/$', views.study, name='study'),
    url('^study/(?P<deck_id>[0-9]+)/get_cards/$', views.get_cards, name='get-cards'),
    url('^delete_deck/$', views.delete_deck, name='delete_deck'),

]

