from django.urls import path,include
from accounts.views import signup ,login,logout

urlpatterns = [
    path('register/',signup,name='register'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
]
