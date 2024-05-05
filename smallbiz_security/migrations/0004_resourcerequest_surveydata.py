# Generated by Django 5.0.4 on 2024-05-05 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smallbiz_security', '0003_survey'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ReqResourceName', models.CharField(help_text='The name of the Resource requested.', max_length=100)),
                ('ReqSourceName', models.CharField(help_text='The source of the Resource requested.', max_length=100)),
                ('ReqLink', models.URLField(help_text="The requested Resource's website.")),
            ],
        ),
        migrations.CreateModel(
            name='SurveyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Q1Data', models.BooleanField(default=False, help_text='Response to Q1')),
                ('Q2Data', models.IntegerField(help_text='Response to Q2')),
                ('Q3Data', models.CharField(help_text='Response to Q3', max_length=3)),
                ('NumEmployees', models.IntegerField(help_text='Number of people employed at the business/organization')),
                ('AcctAge', models.IntegerField(help_text='Age of the account in months')),
                ('City', models.CharField(help_text='City where the business/organization is located', max_length=75)),
                ('State', models.CharField(help_text='Abbreviation of the State where the business/organization is located', max_length=2)),
                ('Free', models.IntegerField(help_text='1 for free account, 0 if not free account')),
                ('Premium', models.IntegerField(help_text='1 for premium account, 0 if not premium account')),
                ('NewSignUp', models.IntegerField(help_text='1 if the business/organization signed up for premium after the survey, 0 if not')),
            ],
        ),
    ]