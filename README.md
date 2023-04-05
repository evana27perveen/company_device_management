# company_device_management Documentaion

* _Project Overview _ *
The project is a Django application for tracking corporate assets, such as phones, tablets, laptops, and other gear handed out to employees. The application allows multiple companies to add all or some of their employees, and delegate one or more devices to employees for a certain period of time. Each company can see when a device was checked out and returned, and each device has a log of what condition it was handed out and returned.

** Models **
The models.py file defines the database models used by the application. There are four models in total:

Company: represents a company that uses the application.
Employee: represents an employee of a company.
Device: represents a device that can be checked out by an employee.
DeviceLog: represents a log entry for when a device is checked out or returned by an employee.
The relationships between these models are as follows:

A Company can have many Employees.
An Employee belongs to one Company.
A Device can be checked out by many Employees.
An Employee can check out many Devices.
A DeviceLog is associated with one Device and one Employee.
The DeviceLog model has several fields to track the state of the device:

checkout_time: the time the device was checked out.
checkout_condition: the condition of the device when it was checked out.
return_time: the time the device was returned.
return_condition: the condition of the device when it was returned.

** Serializers **
The serializers.py file defines the serializers used to convert Django models to and from JSON format. There are five serializers in total, one for each model and two for DeviceLog:

CompanySerializer
EmployeeSerializer
DeviceSerializer
DeviceLogSerializer
DeviceLogCreateSerializer
DeviceLogUpdateSerializer
CompanySerializer, EmployeeSerializer, and DeviceSerializer all use the default serializer behavior provided by Django REST Framework. DeviceLogSerializer is slightly customized to include the related Device and Employee objects in the JSON response.

DeviceLogCreateSerializer and DeviceLogUpdateSerializer are used for creating and updating DeviceLog objects, respectively. They include additional fields for checkout_time, checkout_condition, return_time, and return_condition.

** Views **
The views.py file defines the views used by the application. There are ten views in total:

CompanyListCreateView: handles listing and creating Company objects.
CompanyRetrieveUpdateDestroyView: handles retrieving, updating, and deleting Company objects.
EmployeeListCreateView: handles listing and creating Employee objects.
EmployeeRetrieveUpdateDestroyView: handles retrieving, updating, and deleting Employee objects.
DeviceListCreateView: handles listing and creating Device objects.
DeviceRetrieveUpdateDestroyView: handles retrieving, updating, and deleting Device objects.
DeviceLogListCreateView: handles listing and creating DeviceLog objects.
DeviceLogRetrieveUpdateDestroyView: handles retrieving, updating, and deleting DeviceLog objects.
DeviceLogCreateView: handles creating DeviceLog objects.
DeviceLogUpdateView: handles updating DeviceLog objects.
