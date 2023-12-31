# Generated by Django 4.2.6 on 2023-10-17 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antcrm', '0003_rename_lead_leads'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('created_date', models.DateField()),
            ],
        ),
    ]
