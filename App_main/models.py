from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)


class Employee(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class Device(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    condition_choices = (
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor')
    )
    condition = models.CharField(choices=condition_choices, max_length=4)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)


class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checked_in = models.DateTimeField(null=True, blank=True)
    checked_out = models.DateTimeField(auto_now_add=True)
    condition_choices = (
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('poor', 'Poor')
    )
    condition_in = models.CharField(choices=condition_choices, max_length=4, null=True, blank=True)
    condition_out = models.CharField(choices=condition_choices, max_length=4)
