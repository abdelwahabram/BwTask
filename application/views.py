from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import permissions, viewsets
from .models import Company, Department, Employee, Project
from .serializers import UserSerializer, CompanySerializer, DepartmentSerializer, EmployeeSerializer, ProjectSerializer
from .permissions import IsOwnerOrReadOnly, IsCurrentUserOrReadOnly

# Create your views here.

# new_group, created = Group.objects.get_or_create(name='Employee')

# new_group, created = Group.objects.get_or_create(name='Manager')


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsCurrentUserOrReadOnly]


class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be view and edit companies
    """
    queryset = Company.objects.all().order_by('name')
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated, IsCurrentUserOrReadOnly]


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be view and edit departments
    """
    queryset = Department.objects.all().order_by('name')
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated, IsCurrentUserOrReadOnly]


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be view and edit employees
    """
    queryset = Employee.objects.all().order_by('hired_on')
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be view and edit projects
    """
    queryset = Project.objects.all().order_by('name')
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsCurrentUserOrReadOnly]