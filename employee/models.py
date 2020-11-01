from django.db import models
from fpdf import FPDF

# Create your models here.

LEAVETYPES = (
    ('ANU','ANUAL'),
    ('STU','STUDY'),
    ('SIC','SICK')
    
)

SHIFTTYPES = (
    ('NIG','NIGHT'),
    ('DAY','DURING_DAY'),
   
)

WEEKS = (
    ('W1','WEEK1'),
    ('W2','WEEK2'),
    ('W3','WEEk3'),
    ('W4','WEEK4'),
   
)
MONTHS=(
   ('01','JANUARY'),
    ('02','FEBRUARY'),
    ('03','MARCH'),
    ('04','APRIL'),
    ('05','MAY'),
    ('06','JUNE'),
    ('07','JULY'),
    ('08','AUGUST'),
    ('09','SEPTEMBER'),
    ('10','OCTOBER'),
    ('11','NOVEMBER'),
    ('12','DECEMBER'),
)

class Department(models.Model):
    name=models.CharField(max_length=250)
    description=models.CharField(max_length=250)
    def __str__(self):
        return f'{self.name} {self.description}'
        

class Leave(models.Model):
    startdate=models.DateField()
    enddate=models.DateField()
    leavetype=models.CharField(choices=LEAVETYPES,max_length=3)

    class Meta:
        def __str__(self):
            return self.startdate
        

class Shifts(models.Model):
    name=models.CharField(max_length=25,default='')
    description=models.CharField(max_length=25,default='')

    class Meta:
        def __str__(self):
            return self.name
        

class Employee(models.Model):
    firstname=models.CharField(max_length=250)
    lastname=models.CharField(max_length=250)
    email=models.EmailField(max_length=250)
    onleave=models.BooleanField(default=False)
    department=models.ForeignKey(Department,on_delete=models.DO_NOTHING)


    class Meta:
        def __str__(self):
            return self.firstname

class EmployeeShiftRecords(models.Model):
    employee=models.CharField(max_length=250)
    shift=models.CharField(max_length=250)
    date=models.DateField(auto_now_add=True)
    week=models.CharField(choices=WEEKS,max_length=2)
    month=models.CharField(choices=MONTHS,max_length=2,default='01')

    class Meta:
        def __str__(self):
            return self.date





        


        

