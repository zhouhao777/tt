# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.test import TestCase
from django.utils import timezone

# Create your tests here.
from .models import Question

class QuestionMethonTests(TestCase):
	def test_was_published_recently_with_future_question(self):
		"""
		was_published_recently() should return False for questions whose
        pub_date is in the future.
		"""
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertIs(future_question.was_published_recently(), False)

	def test_was_published_recently_with_old_question(self):
		"""
		was_published_recently() should return False for questions whose
    	pub_date is older than 1 day.
		"""
		time = timezone.now() - datetime.timedelta(days=2)
		old_question = Question(pub_date=time)
		self.assertIs(old_question.was_published_recently(), False)
