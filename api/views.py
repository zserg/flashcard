from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from .models import Deck, Flashcard
from .serializers import DeckSerializer, CardSerializer, RatingSeriallizer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@api_view(['GET', 'POST'])
@csrf_exempt
def decks_list(request):
    #import ipdb; ipdb.set_trace()
    """
    List all decks
    """
    if request.method == 'GET':
        decks = Deck.objects.filter(owner=request.user)
        serializer = DeckSerializer(decks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DeckSerializer(data=request.data)
        if serializer.is_valid():
            if request.user.is_anonymous:
                return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
            else:
                serializer.save(owner=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def deck_details(request, deck_id):
    """
    Deck details
    """
    #import ipdb; ipdb.set_trace()
    if request.method == 'GET':
        #deck = Deck.objects.filter(pk=id, owner=request.user)
        deck = get_object_or_404(Deck, pk=deck_id, owner=request.user)
        serializer = DeckSerializer(deck)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
@csrf_exempt
def cards_list(request, deck_id):
    """
    List all flashcards
    """
    #import ipdb; ipdb.set_trace()
    if request.method == 'GET':
        cards = Flashcard.objects.filter(deck__id=deck_id)
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        try:
            deck = Deck.objects.get(id=deck_id)
        except ObjectDoesNotExist:
            return Response(serializer.errors, status=status.HTTP_401_BAD_REQUEST)

        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            if request.user.is_anonymous:
                return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
            else:
                serializer.save(owner=request.user, deck=deck)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_401_BAD_REQUEST)

@api_view(['GET'])
def card_details(request, deck_id, card_id):
    """
    Card details
    """
    if request.method == 'GET':
        card = get_object_or_404(Flashcard, pk=card_id, deck__id=deck_id, owner=request.user)
        serializer = CardSerializer(card)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_401_BAD_REQUEST)

@api_view(['GET', 'POST'])
def card_ratings(request, deck_id, card_id):
    """
    Card ratings (state)
    """
    if request.method == 'GET':
        card = get_object_or_404(Flashcard, pk=card_id, deck__id=deck_id, owner=request.user)
        serializer = RatingSeriallizer(card)
        return Response(serializer.data)

    elif request.method == 'POST':
        #import ipdb; ipdb.set_trace()
        card = get_object_or_404(Flashcard, pk=card_id, deck__id=deck_id, owner=request.user)
        serializer = RatingSeriallizer(card,data=request.data )
        if serializer.is_valid():
            serializer.save(rating=request.data['rating'])
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_401_BAD_REQUEST)
