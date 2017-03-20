from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.http import JsonResponse

from api.models import Deck, Flashcard
from .forms import CardForm

@login_required
def home(request):
    """
    App home page
    """
    if request.method == 'GET':
        decks = Deck.objects.filter(owner=request.user)
        #import ipdb; ipdb.set_trace()
        context = {'user': request.user, 'decks': decks}
        return render(request, 'flashcardgui/index.html', context)

def profile(request):
    """
    ...
    """
    if request.method == 'GET':
        pass
        #return render(request, 'flashcardgui/index.html',{'user':request.user})

def about(request):
    """
    ...
    """
    if request.method == 'GET':
        return render(request, 'flashcardgui/about.html')

@login_required
def add(request):
    """
    Add new flashcard
    """
    if request.method == 'POST':
        form=CardForm(request.POST)
        #import ipdb; ipdb.set_trace()
        if form.is_valid():
            deck_name = form.cleaned_data['deck']
            question = form.cleaned_data['question']
            answer = form.cleaned_data['answer']
            user = request.user
            Flashcard.objects.create_flashcard(user=user, question=question,
                    answer=answer, deck_name=deck_name)
            return HttpResponseRedirect(reverse('add-card'))
    else:
        form=CardForm()

    return render(request, 'flashcardgui/add.html', {'form': form})

@login_required
def study(request, deck_id):
    """
    Study cards in the deck
    """
    if request.method == 'GET':
        cards = Flashcard.objects.filter(owner=request.user, deck=deck_id)
        context = {'user': request.user, 'cards': cards}
        return render(request, 'flashcardgui/study.html', context)

@login_required
def get_cards(request, deck_id):
    """
    Study cards in the deck
    """
    if request.method == 'GET':
        cards = Flashcard.objects.filter(owner=request.user, deck=deck_id)[:3]
        #data = {'cards': cards}
        data = {'cards': '42'}
        return JsonResponse(data)






