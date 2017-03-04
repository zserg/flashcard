from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.shortcuts import get_object_or_404

from .models import Deck, Flashcard
from .serializers import DeckSerializer, CardSerializer

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

@api_view(['GET'])
def deck_details(request, id):
    """
    Deck details
    """
    #import ipdb; ipdb.set_trace()
    if request.method == 'GET':
        #deck = Deck.objects.filter(pk=id, owner=request.user)
        deck = get_object_or_404(Deck, pk=id, owner=request.user)
        serializer = DeckSerializer(deck)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
@csrf_exempt
def cards_list(request, deck=None):
    """
    List all flashcards
    """
    #import ipdb; ipdb.set_trace()
    if request.method == 'GET':
        if deck:
            cards = Flashcard.objects.filter(deck__id=deck)
        else:
            cards = Flashcard.objects.all()
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CardSerializer(data=request.data)
        if serializer.is_valid():
            if request.user.is_anonymous:
                return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
            else:
                serializer.save(owner=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def card_details(request, id):
    """
    Card details
    """
    if request.method == 'GET':
        card = Card.objects.filter(pk=id)
        serializer = CardSerializer(card)
        return Response(serializer.data)

