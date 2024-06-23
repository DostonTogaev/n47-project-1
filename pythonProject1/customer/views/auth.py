from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from customer.forms import LoginForm, LogoutForm


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

def logout_view(request):
    if request.method == 'POST':
        form = LogoutForm(request.POST)
        if form.is_valid():
            logout(request)
            return redirect('home')  # or any other URL
    else:
        form = LogoutForm()

    return render(request, 'auth/logout.html', {'form': form})