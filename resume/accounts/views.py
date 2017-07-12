from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def login_view(request):
	title = "login"
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect("home")
	context = {"form":form,
			   "title":title
	}

	return render(request, "accounts/login_form.html", context)

def register_view(request):
	title = "Register"
	form = UserRegistrationForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get("password")
		user.set_password(password)
		user.save()
		user.groups.add(Group.objects.get(name='new user'))
		new_user = authenticate(username=user.username, password=password)
		login(request, new_user)
		messages.success(request, "Account created")
		return redirect("create")

	context = {"title":title, "form":form}

	return render(request, "accounts/register_form.html", context)

def logout_view(request):
	if not request.user.is_authenticated():
		messages.error(request, "You must be logged in to do that!")
		return redirect("login")
	else:
		logout(request)
		return redirect("home")
	
