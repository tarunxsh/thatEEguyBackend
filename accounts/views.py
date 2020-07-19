from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm



def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)

            print(new_user)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            
            # Create the user profile
            # Create empty profile associated with the user
            # Profile.objects.create(user=new_user)
            
            # Save the User object
            new = new_user.save()
            # return render(request,'accounts/register_done.html',{'new_user': new_user})
        return redirect('login')

    else:
        user_form = UserRegistrationForm()
        return render(request,'accounts/register.html',{'user_form': user_form})
