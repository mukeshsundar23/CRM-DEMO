from django.contrib import admin
from django.urls import path
from antcrm import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', views.logout, name='logout'),
    path('', views.welcome, name='welcome'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('crm/', login_required(views.crm), name='crm'),
    path('deals_dashboard/', login_required(views.deals_dashboard), name='deals_dashboard'),
    path('leads_dashboard/', login_required(views.leads_dashboard), name='leads_dashboard'),
    path('analytics/', login_required(views.analytics), name='analytics'),
    path('deals_list/', login_required(views.deals_list), name='deals_list'),
    path('deals_form/', login_required(views.deals_form), name='deals_form'),
    path('deals/update/<int:deal_id>/', login_required(views.deals_update), name='deals_update'),
    path('deals/delete/<int:deal_id>/', login_required(views.deals_delete), name='deals_delete'),
    path('leads_list/', login_required(views.leads_list), name='leads_list'),
    path('leads_form/', login_required(views.leads_form), name='leads_form'),
    path('leads/update/<int:lead_id>/', login_required(views.leads_update), name='leads_update'),
    path('leads/delete/<int:lead_id>/', login_required(views.leads_delete), name='leads_delete'),
]
