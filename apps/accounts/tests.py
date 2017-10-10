# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from .views import index



class SignUpTests(TestCase):
    def setUp(self):
        url = reverse('accounts:index')
        self.response = self.client.get(url)

    def test_index_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_index_url_resolves_index_view(self):
        view = resolve('/')
        self.assertEquals(view.func, index)  
