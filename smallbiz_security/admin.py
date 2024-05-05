from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from smallbiz_security.models import (
    Source, Category, Resource, ResourceRequest, CustomerData, Survey, SurveyData)
# Register your models here.


class SourceAdmin(ImportExportModelAdmin):
    list_display = ['SourceName']
    list_filter = ['SourceName']


class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['CategoryName']
    list_filter = ['CategoryName']


class ResourceAdmin(ImportExportModelAdmin):
    list_display = ['ResourceName', 'SourceName',
                    'CategoryName', 'Link', 'DateUploaded']
    list_filter = ['ResourceName', 'SourceName']


class ResourceRequestAdmin(ImportExportModelAdmin):
    list_display = ['Resource_Name', 'Source_Name', 'Link']
    list_filter = ['Resource_Name', 'Source_Name']


class CustomerDataAdmin(ImportExportModelAdmin):
    list_display = ['Year', 'Month', 'Free', 'Premium']
    list_filter = ['Year', 'Month', 'Free', 'Premium']


class SurveyAdmin(ImportExportModelAdmin):
    list_display = ['Q1', 'Q2', 'Q3']
    list_filter = ['Q1', 'Q2', 'Q3']


class SurveyDataAdmin(ImportExportModelAdmin):
    list_display = ['id', 'Q1Data', 'Q2Data', 'Q3Data', 'NumEmployees',
                    'AcctAge', 'City', 'State', 'Free', 'Premium', 'NewSignUp']
    list_filter = ['id', 'Q1Data', 'Q2Data', 'Q3Data', 'AcctAge', 'NewSignUp']


admin.site.register(Source, SourceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(ResourceRequest, ResourceRequestAdmin)
admin.site.register(CustomerData, CustomerDataAdmin)
admin.site.register(Survey, SurveyAdmin)
admin.site.register(SurveyData, SurveyDataAdmin)
