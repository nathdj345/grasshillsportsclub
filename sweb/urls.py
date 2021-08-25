from django.urls import path
from . import views
urlpatterns = [
	path('',views.home,name='home'),
	path('home.html',views.home,name='home'),
	path('contact.html',views.contact,name='contact'),
	path('classes.html',views.classes,name='classes'),
	path('news.html',views.news,name='news'),
	path('newsdetail.html',views.newsdetail,name='newsdetail'),
	path('schedule.html',views.schedule,name='schedule'),
	path('trainers.html',views.trainers,name='trainers'),
	path('about.html',views.about,name='about'),
]
