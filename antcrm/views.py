from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import LeadForm, DealForm, CustomerForm
from .models import Deals, Leads, Customers
from django.db.models import Q
from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator





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
    deals_list = Deals.objects.all()  # Replace 'Customers' with the actual name of your model
    paginator = Paginator(deals_list, 10)  # Show 10 customers per page

    page = request.GET.get('page')
    deals = paginator.get_page(page)

    return render(request, 'deals_list.html', {'deals': deals})

@login_required
def deals_search(request):
    deal_search_query = request.GET.get('search')

    if deal_search_query:
        deals = Deals.objects.filter(Q(deal_name__icontains=deal_search_query) | Q(client__icontains=deal_search_query))
        if deals:
            # If results are found, display a "Found" message
            messages.info(request, f'Results found for "{deal_search_query}"')
        else:
            # If no results are found, display a "Not Found" message
            messages.warning(request, f'No results found for "{deal_search_query}"')
    else:
        deals = Deals.objects.all()

    context = {'deals': deals, 'search_query': deal_search_query}
    return render(request, 'deals_list.html', context)



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
    leads_list = Leads.objects.all()  # Replace 'Customers' with the actual name of your model
    paginator = Paginator(leads_list, 10)  # Show 10 customers per page

    page = request.GET.get('page')
    leads = paginator.get_page(page)

    return render(request, 'leads_list.html', {'leads': leads})

@login_required
def leads_search(request):
    lead_search_query = request.GET.get('search')

    if lead_search_query:
        leads = Leads.objects.filter(Q(first_name__icontains=lead_search_query) | Q(last_name__icontains=lead_search_query))
        if leads:
            # If results are found, display a "Found" message
            messages.info(request, f'Results found for "{lead_search_query}"')
        else:
            # If no results are found, display a "Not Found" message
            messages.warning(request, f'No results found for "{lead_search_query}"')
    else:
        leads = Leads.objects.all()

    context = {'leads': leads, 'search_query': lead_search_query}
    return render(request, 'leads_list.html', context)


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



@login_required
def customers_list(request):
    customers_list = Customers.objects.all()  # Replace 'Customers' with the actual name of your model
    paginator = Paginator(customers_list, 10)  # Show 10 customers per page

    page = request.GET.get('page')
    customers = paginator.get_page(page)

    return render(request, 'customers_list.html', {'customers': customers})


@login_required
def customers_search(request):
    customer_search_query = request.GET.get('search')

    if customer_search_query:
        customers = Customers.objects.filter(Q(first_name__icontains=customer_search_query) | Q(last_name__icontains=customer_search_query))
        if customers:
            # If results are found, display a "Found" message
            messages.info(request, f'Results found for "{customer_search_query}"')
        else:
            # If no results are found, display a "Not Found" message
            messages.warning(request, f'No results found for "{customer_search_query}"')
    else:
        customers = Customers.objects.all()

    context = {'customers': customers, 'search_query': customer_search_query}
    return render(request, 'customers_list.html', context)

@login_required
def customers_form(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers_list')  # Redirect to the leads list view
    else:
        form = CustomerForm()

    return render(request, 'customers_form.html', {'form': form})

@login_required
def customers_update(request, customer_id):
    customer = get_object_or_404(Customers, pk=customer_id)  # Use 'pk' instead of 'lead_id'

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers_list')
    else:
        form = CustomerForm(instance=customer)

    return render(request, 'customers_update.html', {'form': form, 'customer': customer})

@login_required
def customers_delete(request, customer_id):
    customer = get_object_or_404(Customers, pk=customer_id)  # Use 'pk' instead of 'lead_id
    if request.method == 'POST':
        customer.delete()
        return redirect('customers_list')
    return render(request, 'customers_delete.html', {'customers': customer})