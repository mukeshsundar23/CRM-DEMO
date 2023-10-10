from django.contrib import admin
from django.urls import path
from antcrm import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('logout', views.logout, name='logout'),
    path('', views.welcome, name='welcome'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('crm', views.crm, name='crm')
]
