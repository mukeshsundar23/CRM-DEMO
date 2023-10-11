from django.db import models

class Deals(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    class Meta:
        app_label = 'antcrm'

class Leads(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email_address = models.EmailField()
    address = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    lead_score = models.IntegerField(blank=True, null=True)
    lead_owner = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True, null=True)
    next_follow_up_date = models.DateField(blank=True, null=True)
    lead_source = models.CharField(max_length=255, blank=True, null=True)
    lead_type = models.CharField(max_length=255, blank=True, null=True)
    campaign = models.CharField(max_length=255, blank=True, null=True)
    authority = models.CharField(max_length=255, blank=True, null=True)
    need = models.TextField(blank=True, null=True)
    timeline = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'antcrm'


