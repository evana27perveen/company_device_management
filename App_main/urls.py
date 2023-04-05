from django.urls import path
from .views import *

app_name = "App_main"

urlpatterns = [
    path('companies/', CompanyListCreateView.as_view()),  # Unit test done
    path('companies/<int:pk>/', CompanyRetrieveUpdateDestroyView.as_view()),  # Unit test done
    path('employees/', EmployeeListCreateView.as_view()),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view()),
    path('devices/', DeviceListCreateView.as_view()),
    path('devices/<int:pk>/', DeviceRetrieveUpdateDestroyView.as_view()),
    path('devicelogs/', DeviceLogListCreateView.as_view()),
    path('devicelogs/<int:pk>/', DeviceLogRetrieveUpdateDestroyView.as_view()),
    path('devicelogs/create/', DeviceLogCreateView.as_view()),
    path('devicelogs/update/<int:pk>/', DeviceLogUpdateView.as_view()),
]
