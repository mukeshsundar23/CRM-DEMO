# Generated by Django 4.2.6 on 2023-10-11 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antcrm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('status', models.CharField(max_length=20)),
                ('source', models.CharField(max_length=50)),
                ('assigned_to', models.CharField(max_length=50)),
                ('lead_quality', models.CharField(max_length=10)),
                ('lead_score', models.IntegerField()),
                ('notes', models.TextField()),
                ('created_date', models.DateField()),
                ('last_contacted', models.DateField()),
                ('next_followup_date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Leads',
        ),
    ]
