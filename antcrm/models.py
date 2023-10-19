from django.db import models
from django.contrib.auth.models import User


class Deals(models.Model):
    deal_id = models.AutoField(primary_key=True)
    deal_name = models.CharField(max_length=255, default='Default Name')
    stage = models.CharField(max_length=255, default='Default Stage')
    activity = models.CharField(max_length=255, default='Default Activity')
    client = models.CharField(max_length=255, default='Default Client')
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    responsible = models.CharField(max_length=255, default='Default Responsible')
    created = models.DateTimeField(auto_now_add=True)
    customer_journey = models.CharField(max_length=255, default='Default Journey')

    class Meta:
        app_label = 'antcrm'


class Leads(models.Model):
    # Lead ID will be automatically created as a primary key
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    status = models.CharField(max_length=20)
    source = models.CharField(max_length=50)
    assigned_to = models.CharField(max_length=50)
    lead_quality = models.CharField(max_length=10)
    lead_score = models.IntegerField()
    notes = models.TextField()
    created_date = models.DateField()
    last_contacted = models.DateField()
    next_followup_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Customers(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    created_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

IMPORTANCE_CHOICES = (
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
)

class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    time = models.DateTimeField()
    title = models.CharField(max_length=255)
    reminder = models.DateTimeField()
    importance = models.CharField(max_length=10, choices=IMPORTANCE_CHOICES)

    class Meta:
        app_label = 'antcrm'





    


    