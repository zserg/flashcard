from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import login

# Create your views here.
def home(request):
    """
    App home page
    """
    if request.method == 'GET':
        return render(request, 'flashcardgui/index.html',{'user':request.user})

def profile(request):
    """
    ...
    """
    if request.method == 'GET':
        pass
        #return render(request, 'flashcardgui/index.html',{'user':request.user})







