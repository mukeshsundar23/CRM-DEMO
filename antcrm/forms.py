from django import forms
from .models import Deals, Leads, Customers, Tasks


class DealForm(forms.ModelForm):
    class Meta:
        model = Deals
        fields = '__all__'

class LeadForm(forms.ModelForm):
    class Meta:
        model = Leads
        fields = '__all__'  

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = '__all__'

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'