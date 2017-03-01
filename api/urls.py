from django.conf.urls import url
from api import views as api_views

urlpatterns = [
    url(r'^decks/', api_views.decks_list, name='decks-list'),
    url(r'^flashcards/', api_views.flashcards_list, name='flashcards-list'),

]

