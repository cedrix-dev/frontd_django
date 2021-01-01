from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from fdelectro.form import registerForm,signinForm
from django.middleware.csrf import get_token
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from fdelectro.models import register,signin


@csrf_protect
def index(request):
	connecter='OUIIII !'
	return render(request,'fdelectro/index.html',{'connecter':connecter})
	
	

@csrf_exempt
def register1(request):

	if request.method=="POST":
		rgt=registerForm(request.POST)
		print(rgt)
		if rgt.is_valid():
			rgt.save()
			firstname=rgt.cleaned_data['firstName']
			identifiant=rgt.cleaned_data['Identifiant']
			args={'rgt':rgt,'firstname':firstname,'identifiant':identifiant}
			return render(request,'fdelectro/register/index.html',args)
	else:
		return index(request)
	

@csrf_exempt
def signin1(request):
	if request.method=="POST":
		sig=signinForm(request.POST)
		if sig.is_valid():
			my_id=sig.cleaned_data['Identifiant']
			passwd=sig.cleaned_data['password']
			qset=list(register.objects.filter(Identifiant=my_id,password=passwd))
			if len(qset)!=0 :
				arg={'sig':sig,'my_id':my_id,'password':passwd}
				return render(request,'fdelectro/signin/index.html',arg)
			else:
				return  render(request,'fdelectro/signin/notcorrect.html')
	


def home(request):

	sig=signinForm(request.POST)
	print(sig)
	my_id=sig.cleaned_data['Identifiant']
	return render(request,'fdelectro/signin/index.html',{'my_id':my_id})


def about(request):
	return render(request,'fdelectro/aboutus.html')

def command(request):
	return render(request,'fdelectro/command.html')
