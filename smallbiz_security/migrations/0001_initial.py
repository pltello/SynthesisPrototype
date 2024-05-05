# Generated by Django 4.2.5 on 2024-05-04 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(help_text='The name of the Category.', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SourceName', models.CharField(help_text='The name of the Source.', max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ResourceName', models.CharField(help_text='The name of the Resource.', max_length=75)),
                ('Link', models.URLField(help_text="The Resource's website.")),
                ('DateUploaded', models.DateField(help_text='The date that the Resource was uploaded.', null=True)),
                ('CategoryName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smallbiz_security.category')),
                ('SourceName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smallbiz_security.source')),
            ],
        ),
    ]
