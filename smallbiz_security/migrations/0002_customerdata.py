# Generated by Django 5.0.4 on 2024-05-04 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smallbiz_security', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year', models.IntegerField(help_text='Year')),
                ('Month', models.CharField(help_text='Month', max_length=10)),
                ('Free', models.IntegerField(help_text='Number of Free Members')),
                ('Premium', models.IntegerField(help_text='Number of Premium Members')),
            ],
        ),
    ]