from django.shortcuts import render
from .models import *
from django.http import *
from .forms import *
from django.core.mail import send_mail
from EVENTREG import settings

def show(request):
	return render(request,'index.html')
def login(request):
	if request.method=='POST':
		form=eventform(request.POST)
		if form.is_valid():
		
			form.save()
			return HttpResponse('login')
	else:
		form=eventform()
	return render(request,'login.html',{'form':form})
def save(request):
	if request.method=='POST':
		form=eventform(request.POST)
		if form.is_valid():
			
			form.save()
			subject="Confirmation Mail"
			msg="Dear Sir/Ma'am,  We hereby inform you that your event has been published on our site.This is the confirmation Email kindly dont reply to it ... THANK YOU FOR MORE DETAILS CONTACT VISIT:"
			to=form.cleaned_data['Email']
			res=send_mail(subject,msg,settings.EMAIL_HOST_USER,[to])
			return HttpResponse('login')
		#else:
			#return HttpResponse('error')
	else:
		form=eventform()
	return render(request,'login.html',{'form':form})	
def show2(request):
	form=event.objects.all()
	return render(request,'show.html',{'form':form})
	
def about(request):
	return render(request,'about.html')
def contact(request):
	return render(request,'contact.html')

# Create your views here.
