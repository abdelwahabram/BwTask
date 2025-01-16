from django.contrib.auth.models import User
from .models import Company, Department, Employee, Project

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ['url', 'name', 'departments_counter', 'employees_counter', 'projects_counter']


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Department
        fields = ['url', 'name', 'company', 'employees_counter', 'projects_counter']


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['url', 'name','description', 'company', 'department', 'start_date', 'end_date', 'assigned_employee']


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ['url', 'user','designation', 'company', 'department', 'mobile_number', 'address', 'hired_on']