"""
URL configuration for MyProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from smallbiz_security import views
from smallbiz_security.views import FormSuccessView, ResourceRequestFormView, SurveyFormView
from rest_framework import routers
from smallbiz_security import api_views

router = routers.DefaultRouter()
router.register(r'customer-data', api_views.CustomerDataViewSet)
router.register(r'survey-data', api_views.SurveyDataViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='index'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('resource-search', views.resource_search, name='resource search'),
    path('resource-list', views.resource_list, name='resource list'),
    path('entry_success', FormSuccessView.as_view(), name='form_success'),
    path('resource-request-form', ResourceRequestFormView.as_view(),
         name='resource-request-form'),
    path('survey-form', SurveyFormView.as_view(),
         name='survey-form')
]

if settings.DEBUG:

    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
