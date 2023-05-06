from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from accounts.forms import LoginForm

def user_login(request):
    if request.method ==  "POST":
        form =  LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username']
            password = cd['password']
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return redirect('login')
        else:
            return redirect('login')
    else:
        form = LoginForm()
        cx = {'form': form}
        template_name = 'accounts/login.html'
        return render(request, template_name, cx)


def user_logout(request):
    logout(request)
    return redirect('login')