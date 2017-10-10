# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
import random 


def index(request):
    return render(request, 'accounts/index.html')

def home(request):
    return render(request, 'accounts/home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


