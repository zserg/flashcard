from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

from .models import Deck, Flashcard
from .serializers import DeckSerializer

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
        decks = Deck.objects.all()
        serializer = DeckSerializer(decks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DeckSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def deck_details(request, id):
    """
    Deck details
    """
    if request.method == 'GET':
        #import ipdb; ipdb.set_trace()
        deck = Deck.objects.get(pk=id)
        serializer = DeckSerializer(deck)
        return Response(serializer.data)

def flashcards_list(request):
    return Response("yes")

