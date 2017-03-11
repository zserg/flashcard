from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from flashcardgui import views


urlpatterns = [
    url('^account/', include('django.contrib.auth.urls')),
    url('^account/signup/$', views.signup, name='signup'),
    url('^$', views.index, name='index'),
   # url(r'^decks/(?P<deck_id>[0-9]+)/$', api_views.deck_details, name='deck-details'),
    # url(r'^decks/(?P<deck_id>[0-9]+)/cards/$', api_views.cards_list, name='cards-list'),
    # url(r'^decks/(?P<deck_id>[0-9]+)/cards/(?P<card_id>[0-9]+)/$',
    #       api_views.card_details, name='card-details'),
    # url(r'^decks/(?P<deck_id>[0-9]+)/cards/(?P<card_id>[0-9]+)/ratings/$',
    #       api_views.card_ratings, name='card-ratings'),

]

