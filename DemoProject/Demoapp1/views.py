from django.contrib import messages, auth
from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def login1(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid username or password")
            return redirect('login1')
    return render(request, "login1.html")



def register1(request,):
    if request.method=='POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username exist")
                return redirect('register1')

            elif User.objects.filter(email=email).exists():
                messages.info(request,"email exist")
                return redirect('register1')

            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
                user.save();
                return redirect('login1')

        else:
            messages.info(request,"password not matching")
            return redirect('register1')

        return redirect('/')

    return render(request, "register1.html")


def logout(request):
    auth.logout(request)
    return redirect('/')