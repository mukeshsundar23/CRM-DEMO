from django.contrib import admin
from django.urls import path
from antcrm import views


urlpatterns = [
    path('admin', admin.site.urls),
    path('logout', views.logout, name='logout'),
    path('', views.welcome, name='welcome'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('crm', views.crm, name='crm'),
    path('deals_dashboard', views.deals_dashboard, name='deals_dashboard'),
    path('leads_dashboard', views.leads_dashboard, name='leads_dashboard'),
    path('analytics', views.analytics, name='analytics'),
    path('deals_list', views.deals_list, name='deals_list'),
    path('deals_form', views.deals_form, name='deals_form'),
    path('leads', views.leads, name='leads'),
]

