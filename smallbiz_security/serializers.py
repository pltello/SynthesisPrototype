from rest_framework import serializers
from .models import CustomerData, SurveyData


class CustomerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerData
        fields = ['Year', 'Month', 'Free', 'Premium']


class SurveyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyData
        fields = ['id', 'Q1Data', 'Q2Data', 'Q3Data', 'NumEmployees',
                  'AcctAge', 'City', 'State', 'Free', 'Premium', 'NewSignUp']
