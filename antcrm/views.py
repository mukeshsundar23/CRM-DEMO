from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import LeadForm, DealForm
from .models import Deals, Leads



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

@login_required
def deals_dashboard(request):
    return render(request, 'deals_dashboard.html')

@login_required
def leads_dashboard(request):
    return render(request, 'leads_dashboard.html')

@login_required
def analytics(request):
    return render(request, 'analytics.html')

@login_required
def deals_list(request):
    deals = Deals.objects.all()  # Fetch all deals from the database
    return render(request, 'deals_list.html', {'deals': deals})

@login_required
def deals_form(request):
    if request.method == 'POST':
        form = DealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('deals_list')  # Redirect to the deals list view
    else:
        form = DealForm()
    return render(request, 'deals_form.html', {'form': form})

@login_required
def deals_update(request, deal_id):
    deal = get_object_or_404(Deals, deal_id=deal_id)

    if request.method == 'POST':
        form = DealForm(request.POST, instance=deal)
        if form.is_valid():
            form.save()
            return redirect('deals_list')
    else:
        form = DealForm(instance=deal)

    return render(request, 'deals_update.html', {'form': form, 'deal': deal})

@login_required
def deals_delete(request, deal_id):
    deal = get_object_or_404(Deals, deal_id=deal_id)
    if request.method == 'POST':
        deal.delete()
        return redirect('deals_list')
    return render(request, 'deals_delete.html', {'deal': deal})

@login_required
def leads_list(request):
    leads = Leads.objects.all()  # Fetch all deals from the database
    return render(request, 'leads_list.html', {'leads': leads})

@login_required
def leads_form(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('leads_list')  # Redirect to the leads list view
    else:
        form = LeadForm()

    return render(request, 'leads_form.html', {'form': form})

@login_required
def leads_update(request, lead_id):
    lead = get_object_or_404(Leads, pk=lead_id)  # Use 'pk' instead of 'lead_id'

    if request.method == 'POST':
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect('leads_list')
    else:
        form = LeadForm(instance=lead)

    return render(request, 'leads_update.html', {'form': form, 'lead': lead})

@login_required
def leads_delete(request, lead_id):
    lead = get_object_or_404(Leads, pk=lead_id)  # Use 'pk' instead of 'lead_id
    if request.method == 'POST':
        lead.delete()
        return redirect('leads_list')
    return render(request, 'leads_delete.html', {'lead': lead})





