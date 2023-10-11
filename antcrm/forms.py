from django import forms
from .models import Deals
from .models import Leads

class DealForm(forms.ModelForm):
    class Meta:
        model = Deals
        fields = '__all__'

class LeadForm(forms.ModelForm):
    class Meta:
        model = Leads
        fields = '__all__'  