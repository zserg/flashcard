from django.conf.urls import url
from api import views as api_views

urlpatterns = [
    url(r'^decks/$', api_views.decks_list, name='decks-list'),
    url(r'^decks/(?P<id>[0-9]+)/$', api_views.deck_details, name='deck-details'),
    url(r'^cards/$', api_views.cards_list, name='cards-list'),

]

