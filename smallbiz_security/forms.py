from django import forms
from .models import ResourceRequest, Survey


class SearchForm(forms.Form):
    search = forms.CharField(required=False, min_length=3)
    search_in = forms.ChoiceField(
        required=False, choices=(("ResourceName", "Resource"), ("SourceName", "Source"),
                                 ("CategoryName", "Category"))
    )


class ResourceRequestForm(forms.ModelForm):
    class Meta:
        model = ResourceRequest
        fields = ['Resource_Name', 'Source_Name', 'Link']


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['Q1', 'Q2', 'Q3']
