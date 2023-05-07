from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from accounts.forms import LoginForm, NewUserForm

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
                messages.success(request, 'welcome'+ ' ' + request.user.username)
                return redirect('home')
            else:
                messages.warning(request, 'please check your username or password')
                return redirect('login')
        else:
            messages.error(request, 'please contact admin')
            return redirect('login')
    else:
        form = LoginForm()
        cx = {'form': form}
        template_name = 'accounts/login.html'
        return render(request, template_name, cx)


def user_logout(request):
    logout(request)
    return redirect('home')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="accounts/register.html", context={"form":form})