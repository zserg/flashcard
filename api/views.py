from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def decks_list(request):
    #import ipdb; ipdb.set_trace()
    return Response("yes")

def flashcards_list(request):
    return Response("yes")

