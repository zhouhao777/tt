from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,render
from django.views.decorators.csrf import csrf_exempt,csrf_protect 
from django.template.context import RequestContext 
from django.contrib.auth.forms import UserCreationForm



# @csrf_exempt
# @csrf_protect
def login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/tt/')
		#todo change

	username = request.POST.get('username', '')
	password = request.POST.get('password', '')

	user = auth.authenticate(username=username, password=password)

	if user is not None and user.is_active:
		auth.login(request, user)
		return HttpResponseRedirect('/login/')
	else:
		return render(request,'login.html') 



def index(request):
	return render(request,'base.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/tt/')

def register(request):
	if request.method == 'POST':
		print request.POST
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			return HttpResponseRedirect('/tt/')
	else:
		form = UserCreationForm()
	return render(request,'register.html',locals())