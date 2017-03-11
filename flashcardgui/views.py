from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    """
    App home page
    """
    if request.method == 'GET':
        return render(request, 'flashcardgui/index.html',{'user':request.user})


def signup(request):
    """
    User signup
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = User.objects.create(form.cleaned_data['username'],
                                       form.cleaned_data['password'],
                                       form.cleaned_data['email'])
            user.save()
            return redirect('index', 'flashcardgui/index.html')
    else:
        form = UserCreationForm()

    return render(request, 'flashcardgui/signup.html')






