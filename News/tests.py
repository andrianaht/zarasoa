"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.utils import unittest
from News.models import News
from django.contrib.auth.models import User
from datetime import datetime


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
        

class ModelTest(TestCase):
    def setUp(self):
        username = 'andrianaht'; email ='toni@gmail.com';password='123'
        user = User.objects.create_user(username, email, password)
        self.new = News.objects.create(title='TEST 1', body='BODY TEST 1',
        image=None, creator=user
        )
        
    def test_news_created(self):
        print self.new
        self.assertEqual(self.new.title, 'TEST 1')
    