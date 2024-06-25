from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from customer.forms import LoginForm, RegistrationForm


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            user = authenticate(request, phone_number=phone_number, password=password)
            if user:
                login(request, user)
                return redirect('customer')
    else:
        form = LoginForm()

    return render(request, 'auth/login.html', {'form': form})



def logout_page(request):
    if request.method == 'GET   ':
        logout(request)
        return redirect('app/customers.html')
    return render(request,'auth/logout.html')

def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
 # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
 # Set the chosen password
            new_user.set_password(
            user_form.cleaned_data['password'])
 # Save the User object
            new_user.save()
            return render(request,'app/customer.html', {'new_user': new_user})
    else:
        user_form = RegistrationForm()
    return render(request,'auth/register.html', {'user_form': user_form})