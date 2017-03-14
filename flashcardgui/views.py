from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import login
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    """
    App home page
    """
    if request.method == 'GET':
        decks = Deck.objects.filter(owner=request.user)
        context = {'user': request.user, 'decks': decks}
        return render(request, 'flashcardgui/index.html', context)

def profile(request):
    """
    ...
    """
    if request.method == 'GET':
        pass
        #return render(request, 'flashcardgui/index.html',{'user':request.user})







