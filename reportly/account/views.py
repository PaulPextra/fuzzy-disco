from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password

# Password Validation Function
def password_is_strong(password):
    '''Password Validation Function'''
    if (len(password) < 6) or (len(password)>16):
        isValid = False
    elif not any(char.isdigit() for char in password):
        isValid = False
    elif not any(char.islower() for char in password):
        isValid = False
    elif not any(char.isupper() for char in password):
        isValid = False
    else:
        isValid = True
        
    return isValid

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            return redirect('attendance:all_books')
        else:
            messages.warning(request, 'Please enter a valid username and password')
            
    return render(request, 'registration/login.html')

def signup_view(request):
    if request.method == 'POST':
        data = {key:request.POST.get(key) for key in request.POST.keys()}

        # remove crsf middleware token from the data if it exist.
        if 'csrfmiddlewaretoken' in data.keys():
            data.pop('csrfmiddlewaretoken') 

        # remove both passwords from the data.
        password = data.pop('password')
        re_password = data.pop('re_password')

        # if both passwords are equal and are valid, add just one of them to the data.
        if password == re_password:
            if password_is_strong(password): # checking if the password is strong.
                data['password'] = make_password(password) # adding the valid password to the data.
                try:
                    User.objects.create(**data, is_active=True) # creating a new user
                    messages.success(request, 'Account Successfully Created')
                except Exception as e:
                    print(e)
                    messages.warning(request, str(e))
            else:
                messages.warning(request, 'Password length should not be less than 6')
                messages.warning(request, 'Password should contain at least:\na number, \na lowercase letter [a-z] and \nAn uppercase letter [A-Z]')
        else:
            messages.warning(request, 'Please enter matching passwords')

    return render(request, 'registration/signup.html')