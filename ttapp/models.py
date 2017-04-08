# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

# Create your models here.
@python_2_unicode_compatible 
class Question(models.Model):
    question_text = models.CharField(max_length=190)
    pub_date = models.DateTimeField('date published')
    views = models.IntegerField(default=0)
    
    def __str__(self):
		return self.question_text
		
    def was_published_recently(self):
		return timezone.now()-datetime.timedelta(days=1)<=self.pub_date<=timezone.now()

@python_2_unicode_compatible 
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
    	return self.choice_text
