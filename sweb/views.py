from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request,'home.xml',{})

def contact(request):
	if request.method == 'POST' :
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		message = request.POST['message']
		send_mail(
			name,
			message,
			email,
			['djdebo345@gmail.com'],
			)

		return render(request,'contact.xml',{'name': name})
	else :
		return render(request,'contact.xml',{})

def classes(request):
	return render(request,'classes.xml',{})

def news(request):
	return render(request,'news.xml',{})

def newsdetail(request):
	return render(request,'newsdetail.xml',{})

def schedule(request):
	return render(request,'schedule.xml',{})

def trainers(request):
	return render(request,'trainers.xml',{})

def about(request):
	return render(request,'about.xml',{})

