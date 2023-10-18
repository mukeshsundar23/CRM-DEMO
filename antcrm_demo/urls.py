from django.contrib import admin
from django.urls import path, include
from antcrm import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', views.logout, name='logout'),
    path('calendar/', views.calendar, name='calendar'),
    path('calendar/tasks/', views.tasks, name='tasks'),
    path('', views.welcome, name='welcome'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('crm/', login_required(views.crm), name='crm'),
    path('deals_dashboard/', login_required(views.deals_dashboard), name='deals_dashboard'),
    path('leads_dashboard/', login_required(views.leads_dashboard), name='leads_dashboard'),
    path('analytics/', login_required(views.analytics), name='analytics'),
    path('deals_list/', login_required(views.deals_list), name='deals_list'),
    path('deals/search/', login_required(views.deals_search), name='deals_search'),
    path('deals_form/', login_required(views.deals_form), name='deals_form'),
    path('deals/update/<int:deal_id>/', login_required(views.deals_update), name='deals_update'),
    path('deals/delete/<int:deal_id>/', login_required(views.deals_delete), name='deals_delete'),
    path('leads_list/', login_required(views.leads_list), name='leads_list'),
    path('leads/search/', login_required(views.leads_search), name='leads_search'),
    path('leads_form/', login_required(views.leads_form), name='leads_form'),
    path('leads/update/<int:lead_id>/', login_required(views.leads_update), name='leads_update'),
    path('leads/delete/<int:lead_id>/', login_required(views.leads_delete), name='leads_delete'),
    path('customers_list/', login_required(views.customers_list), name='customers_list'),
    path('customers/search/', login_required(views.customers_search), name='customers_search'),
    path('customers_form/', login_required(views.customers_form), name='customers_form'),
    path('customers/update/<int:customer_id>/', login_required(views.customers_update), name='customers_update'),
    path('customers/delete/<int:customer_id>/', login_required(views.customers_delete), name='customers_delete'),
]
