from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse
from .forms import MessageForm,MsgForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import MessageModel,Message




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
               
                msgmodel = MessageModel(receiver=User.objects.get(username=request.POST['dropdown']),
                receiver_name = request.POST['dropdown'],
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
    # print(username)
    # return HttpResponse('{} Selected'.format(username))
    msgForm = MsgForm(request.POST or None)
    if msgForm.is_valid():
        msgModel = Message(receiver_name = username, sender_name = request.user, message = msgForm.cleaned_data['message'])
        msgModel.save()

        msgForm = MessageForm()
   
    send_messages = Message.objects.all().filter(receiver_name = username).filter(sender_name = request.user)
    received_messages =  Message.objects.all().filter(receiver_name = request.user).filter(sender_name = username)
    return render(request,'ind-users.html',{'form' : msgForm,'messages':send_messages,'receiver': username,'received' : received_messages})
