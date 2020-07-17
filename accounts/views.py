from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.

def signup(request):
    if request.method == 'POST' :
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if  password1==password2:
            if User.objects.filter(username=username).exists():
                print('username taken')
                messages.info(request,'username taken')
                return redirect('register')
                

            elif  User.objects.filter(email=email).exists():
                print('email taken')
                messages.info(request,'email taken')
                return redirect('register')   
                
            else:
                user = User.objects.create_user(username=username,email=email,password=password1,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
                return redirect('login')
            

        else:
            print('password not matching')
            messages.info(request,'password not matching')
            return redirect('register')
            
        return redirect('login')



    else:
        return render(request,'signup.html')


def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
    
        if user is not None:
            auth.login(request,user)
            return redirect('index')

        else:
            messages.info(request,'invalid credentials') 
            return redirect('register')   
        

    else:    
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')