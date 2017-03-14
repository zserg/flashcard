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


# def signup(request):
#     """
#     User signup
#     """
#     import ipdb; ipdb.set_trace()
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = User.objects.create(form.cleaned_data['username'],
#                                       form.cleaned_data['password1'])
#             user.save()
#             return redirect('index', 'flashcardgui/index.html')
#     else:
#         form = UserCreationForm()

#     return render(request, 'registration/signup.html', {'form':form})






