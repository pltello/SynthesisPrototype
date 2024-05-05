from rest_framework import viewsets
from .models import CustomerData, SurveyData
from .serializers import CustomerDataSerializer, SurveyDataSerializer


class CustomerDataViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing customer data.
    """
    queryset = CustomerData.objects.all()
    serializer_class = CustomerDataSerializer


class SurveyDataViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing customer data.
    """
    queryset = SurveyData.objects.all()
    serializer_class = SurveyDataSerializer
