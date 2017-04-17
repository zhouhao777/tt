from django.conf.urls import url
from . import views

app_name = 'ttapp'
urlpatterns = [
    #ex:/tt/
	url(r'^$', views.IndexView.as_view(), name='index'),
	#ex:/tt/3/
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
     # ex: /polls/5/results/
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
     # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # crawler
    url(r'^crawler/$', views.crawler_list, name='crawler'),
    url(r'^query/$',views.query_crawler, name ='query'), 
]
