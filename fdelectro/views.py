from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from fdelectro.form import registerForm,signinForm
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

#from django.middleware.csrf import CsrfViewMiddleware 
# Create your views here.

@csrf_protect
def index(request):
	connecter='OUIIII !'
	return render(request,'fdelectro/index.html',{'connecter':connecter})
	#return render(request,'fdelectro/index.html',{'connecter':connecter})
	
	

@csrf_exempt
def register(request):

	if request.method=="POST":
		rgt=registerForm(request.POST)
		if rgt.is_valid():
			rgt.save()
			firstname=rgt.cleaned_data['firstName']
			identifiant=rgt.cleaned_data['Identifiant']
			args={'rgt':rgt,'firstname':firstname,'identifiant':identifiant}
	return render(request,'fdelectro/register/index.html',args)
	
	

def about(request):
	
	connecter='OUIIII !'
	return render(request,'fdelectro/index.html',{'connecter':connecter})
def command(request):
	
	connecter='OUIIII !'
	return render(request,'fdelectro/index.html',{'connecter':connecter})



