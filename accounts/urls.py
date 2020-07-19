from django.urls import path , include
#from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
	#auth urls provided by django | No views required 
	path('' , include('django.contrib.auth.urls')),
	path('register/',views.register,name='register'),
]