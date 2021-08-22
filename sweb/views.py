from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request,'home.html',{})

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

		return render(request,'contact.html',{'name': name})
	else :
		return render(request,'contact.html',{})

def classes(request):
	return render(request,'classes.html',{})

def news(request):
	return render(request,'news.html',{})

def newsdetail(request):
	return render(request,'newsdetail.html',{})

def schedule(request):
	return render(request,'schedule.html',{})

def trainers(request):
	return render(request,'trainers.html',{})

def about(request):
	return render(request,'about.html',{})

