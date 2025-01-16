from django.contrib import admin
from .models import Company, Department, Employee, Project
# Register your models here.
admin.site.register(Company)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Project)