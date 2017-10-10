# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect, get_object_or_404

def signup(request):
   
    return render(request, 'accounts/index.html')
