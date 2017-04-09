# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.db.models import Sum,Count

from .models import Question,Choice,Crawler


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'ttapp/index.html'
    model = Question
    # context_object_name = 'new_question_list'

    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     # hot_question_list = Choice.objects.order_by('pub_date')[:5]
    #     return Question.objects.order_by('-pub_datepub_date')[:2]
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['latest_question_list'] = Question.objects.order_by('-pub_date')[:5]
        #select sum(votes) as vote,question_id as qid from ttapp_choice group by question_id order by vote desc;
        #在question上面弄个反向查询，然后再sum，再order_by，再再再取前5个
        #Question.objects.annotate(sumvotes=Sum('choice__votes')).order_by('-sumvotes')
        context['hot_question_list'] = Question.objects.annotate(sumvotes=Sum('choice__votes')).order_by('-sumvotes')[:5]
        return context

def crawler_list(request):

    result = Crawler.objects.values('code').annotate(dcount=Count('code')).order_by('-dcount')[:10]
    return render(request, 'ttapp/crawler.html', {'result':result})
def query_crawler(request,query_time):
    result = Crawler.objects.values('code').annotate(dcount=Count('code')).order_by('-dcount')[:10].filter('ctime'>'query_time')
    return render(request, 'ttapp/crawler.html', {'result':result})

class DetailView(generic.DetailView):
    model = Question
    template_name = 'ttapp/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'ttapp/results.html'
		



def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except(KeyError, Choice.DoesNotExist):
		return render(request, 'ttapp/detail.html',{
			'question':question,
			'error_message':"you didn't select a choice",
		})
	else:
		selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('ttapp:results', args=(question.id,)))
