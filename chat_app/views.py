from django.shortcuts import render
from .forms import MessageForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import MessageModel


# Create your views here.

# @login_required
def home(request):
    sender = authenticate(username='Shaji', password='shajithomas1253')
    if sender is not None:
        login(request, sender)
        print("{} authenticated".format(request.user))
        users = User.objects.all().filter(is_staff=False)

        form = MessageForm(request.POST or None)
        if form.is_valid():
            print()

            msgmodel = MessageModel(receiver=User.objects.get(username=request.POST['dropdown']),
                                    sender_name=request.user,
                                    message=form.cleaned_data['message'])
            msgmodel.save()

        else:
            print("Error")

    return render(request, 'index.html', {'messageform': form, 'users': users})