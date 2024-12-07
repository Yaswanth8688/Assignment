from django.shortcuts import render,HttpResponse,redirect
from .models import users
from .forms import userForm
# Create your views here.
def hello(request):
    return render(request, 'hello.html')


def new_user(request):
    new_user=userForm()
    if request.method == 'POST':
        new_user=userForm(request.POST)
        if new_user.is_valid():
            new_user.save()
            return redirect('myapp:users')
        else:
            return HttpResponse("<h1>Data is invalid<h1>")
    return render(request,'new_user.html',context={'new_user':new_user})

def allUsers(request):
    user = users.objects.all()
    return render(request,'users.html',context={'users':user})


def singleUser(request,id):
    user = users.objects.get(id=id)
    return render(request,'single_user.html',context={'users':user})