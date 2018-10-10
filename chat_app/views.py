from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse
from .forms import MessageForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import MessageModel




def login_func(request):

    if request.method == 'POST':
        user = authenticate(username = request.POST['username'],password = request.POST['password'])
        if user is not None:
            login(request,user)
            print("{} authenticated".format(request.user))
            return redirect('home')
        else:
            print('Wrong credentials')

    return render(request,'login.html')


def home(request):
        if request.user.is_authenticated:
            print("{} authenticated".format(request.user))
            users = User.objects.all().filter(is_staff=False).exclude(username = request.user)

            form = MessageForm(request.POST or None)
            if form.is_valid():
                print()

                msgmodel = MessageModel(receiver=User.objects.get(username=request.POST['dropdown']),
                                        sender_name=request.user,
                                        message=form.cleaned_data['message'])
                msgmodel.save()

                form = MessageForm()

            else:
                print("Error")

            messages = reversed(MessageModel.objects.all().filter(sender_name=request.user).order_by('-id')[:4])

            return render(request, 'index.html', {'messageform': form, 'users': users, 'messages': messages})
        else:
            return redirect('login')

def list_users(request):
    users = User.objects.all().filter(is_staff=False)
    return render(request, 'users.html', {'users': users})


def message_user(request,username):
    print(username)
    return HttpResponse('{} Selected'.format(username))
    
