from django.urls import path
from . import views
urlpatterns = [
	path('',views.home,name='home'),
	path('home.xml',views.home,name='home'),
	path('contact.xml',views.contact,name='contact'),
	path('classes.xml',views.classes,name='classes'),
	path('news.xml',views.news,name='news'),
	path('newsdetail.xml',views.newsdetail,name='newsdetail'),
	path('schedule.xml',views.schedule,name='schedule'),
	path('trainers.xml',views.trainers,name='trainers'),
	path('about.xml',views.about,name='about'),
]
