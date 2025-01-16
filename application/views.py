from django.shortcuts import render
from django.contrib.auth.models import User, Group
# Create your views here.

new_group, created = Group.objects.get_or_create(name='Employee')

new_group, created = Group.objects.get_or_create(name='Manager')
