from django.shortcuts import render
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def welcome(request):
    return render(request, 'welcome.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('crm')  
    return render(request, 'login.html') 


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log in the user
            login(request, user)
            return redirect('login')  # Redirect to the login page
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def logout(request):
    return render(request, 'logout.html') 


@login_required
def crm(request):
    return render(request, 'crm.html')

def deals_dashboard(request):
    return render(request, 'deals_dashboard.html')

def leads_dashboard(request):
    return render(request, 'leads_dashboard.html')

def analytics(request):
    return render(request, 'analytics.html')

def deals_list(request):
    return render(request, 'deals_list.html')

def deals_form(request):
    return render(request, 'create_deals.html')

def leads(request):
    return render(request, 'leads.html')


