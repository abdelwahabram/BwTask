from django.db import models
from django.contrib.auth.models import User, Group
# from phonenumber_field.phonenumber import PhoneNumber
from phonenumber_field.modelfields import PhoneNumberField
from address.models import AddressField


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=200)
    
    departments_counter = models.PositiveIntegerField(default=0, editable=False)
    
    projects_counter = models.PositiveIntegerField(default=0, editable=False )
    
    employees_counter = models.PositiveIntegerField(default=0, editable=False)

    def __str__(self):
        return str(self.name) + " depart_cnt: " + str(self.departments_counter) + "proj_cnt: " + str(self.projects_counter) + "emp_cnt: " + str(self.employees_counter)
    

    def update_departments_counter(self, value = 1):
        # self.departments_counter = models.Count(Department.objects.filter(company = self))
        self.departments_counter = Department.objects.filter(company = self).count()
        # print("d",self.departments_counter)
        self.save()
    
    def update_projects_counter_counter(self):
        # self.projects_counter += value
        self.projects_counter = Project.objects.filter(company = self).count()
        self.save()
    
    def update_employees_counter(self):
        # self.employees_counter += value
        self.employees_counter = Employee.objects.filter(company = self).count()
        self.save()


class Department(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)

    projects_counter = models.PositiveIntegerField(default=0, editable=False)

    employees_counter = models.PositiveIntegerField(default=0, editable=False)

    def save(self, *args, **kwargs):
        # self.company.update_departments_counter()
        output = super(Department, self).save(*args, **kwargs)
        self.company.update_departments_counter()
        return output
    
    def delete(self, *args, **kwargs):
        
        output =  super(Department, self).delete(*args, **kwargs)
        self.company.update_departments_counter()
        return output
    
    def update_projects_counter(self):
        self.projects_counter = Project.objects.filter(department = self).count()
        self.save()
    
    def update_employees_counter(self):
        self.employees_counter = Employee.objects.filter(department = self).count()
        self.save()


class Employee(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    mobile_number = PhoneNumberField(blank=False)

    address = AddressField(blank=True, null=True)

    designation = models.TextField(max_length=200)

    hired_on = models.DateField(blank=True, null=True)

    # days_employed = models.DurationField()

    def save(self, *args, **kwargs):
        
        output = super(Employee, self).save(*args, **kwargs)

        self.company.update_employees_counter()
        self.department.update_employees_counter()

        return output
    
    def delete(self, *args, **kwargs):
        
        output = super(Employee, self).delete(*args, **kwargs)

        self.company.update_employees_counter()
        self.department.update_employees_counter()

        return output


class Project(models.Model):

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    name = models.CharField(blank=False, null=False, max_length=200)

    description = models.TextField(blank=True, max_length=1200)

    start_date = models.DateField(blank=True)

    end_date = models.DateField(blank=True)

    assigned_employees = models.ManyToManyField(Employee, blank=True)

    def save(self, *args, **kwargs):
        output = super(Project, self).save(*args, **kwargs)

        self.company.update_projects_counter_counter()
        self.department.update_projects_counter()

        return output

