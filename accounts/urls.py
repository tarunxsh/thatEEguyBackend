from django.urls import path , include
#from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

	#auth urls provided by django | No views required 
	path('' , include('django.contrib.auth.urls')),
	path('register/',views.register,name='register'),
]



# auth view builtin urls present in django.contrib.auth.urls

# path('login/', auth_views.LoginView.as_view(), name='login'),
# path('logout/', auth_views.LogoutView.as_view(), name='logout'),

# #password change urls
# path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
# path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),

# # reset password urls
# path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
# path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
# path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
# path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

# Views => TEMPLATES
# PasswordResetView => renders form to reset password => password_reset_form.html
# EMAIL IS SENT WITH FORMAT AS IN password_reset_email.html
# EMAIL SUBJECT  password_reset_subject.txt
# PasswordResetDoneView => EMAIL SUCCESS TEMPLATE => password_reset_done.html
# LINK IS SUCCESSFULLY TO SENT TO USER EMAIL
# LINK OPEN ONLY ONCE ON ONE DEVICE
# PasswordResetConfirmView => NEW PASSWORD SET TEMPLATE => password_reset_confirm.html
# PasswordResetCompleteView => PASSWORD SET SUCCESS TEMPLATE => password_reset_complete.html